# Date & Time Components

Components for collecting dates and times from users.

---

## DatePicker

Date selection interface. Opens native date picker on user's device.

**Properties:**
- `name` - Field identifier (required)
- `label` - Field label (optional)
- `required` - Must select date (default: false)
- `init-value` - Initial date (YYYY-MM-DD format)
- `max-date` - Latest selectable date (YYYY-MM-DD)
- `min-date` - Earliest selectable date (YYYY-MM-DD)

### Basic DatePicker

```json
{
  "type": "DatePicker",
  "name": "birth_date",
  "label": "Date of Birth",
  "required": true
}
```

### DatePicker with Date Range

```json
{
  "type": "DatePicker",
  "name": "delivery_date",
  "label": "Delivery Date",
  "min-date": "2024-01-01",
  "max-date": "2024-12-31"
}
```

### Form Value

Date stored as string in YYYY-MM-DD format:

```json
${form.birth_date}  // "1990-05-15"
```

### Timezone Considerations

- DatePicker respects device timezone
- Server receives date in user's timezone
- v5.0+ handles timezone conversion better
- Always validate dates server-side for correctness

---

## CalendarPicker (v6.1+)

Full calendar interface with single or range selection.

**Properties:**
- `name` - Field identifier (required)
- `label` - Field label (optional)
- `mode` - `single` (default) or `range`
- `required` - Must select (default: false)
- `init-value` - Initial date(s)
- `max-date` - Latest selectable date (YYYY-MM-DD)
- `min-date` - Earliest selectable date (YYYY-MM-DD)

### Single Date Selection

```json
{
  "type": "CalendarPicker",
  "name": "appointment_date",
  "label": "Choose Appointment Date",
  "mode": "single",
  "min-date": "2024-01-15",
  "max-date": "2024-02-15"
}
```

### Date Range Selection

```json
{
  "type": "CalendarPicker",
  "name": "trip_dates",
  "label": "Select Trip Dates",
  "mode": "range",
  "min-date": "2024-03-01",
  "max-date": "2024-12-31"
}
```

### Form Value

Single date or range:

```json
${form.appointment_date}  // "2024-01-20"
${form.trip_dates}        // {"start": "2024-06-01", "end": "2024-06-15"}
```

### CalendarPicker Advantages over DatePicker

- Full calendar view (better context)
- Range selection for date spans
- Better mobile UX
- Can see adjacent months
- (Requires v6.1+)

---

## Comparing DatePicker vs CalendarPicker

| Feature | DatePicker | CalendarPicker |
|---------|-----------|-----------------|
| Single date | ✓ | ✓ |
| Date range | ✗ | ✓ |
| Wheel/Scroll | ✓ | ✗ |
| Calendar view | ✗ | ✓ |
| Version | v5.0+ | v6.1+ |
| Mobile UX | Native picker | Visual calendar |

---

## Date Format Rules

- Format: **YYYY-MM-DD**
- Example: `2024-03-15` (March 15, 2024)
- Always ISO format regardless of device locale
- Server receives ISO format always

### Converting to/from ISO Format

JavaScript:
```javascript
new Date("2024-03-15").toISOString().split('T')[0]  // "2024-03-15"
```

Python:
```python
from datetime import datetime
datetime.fromisoformat("2024-03-15").strftime("%Y-%m-%d")  # "2024-03-15"
```

---

## Date Picker in Forms

Typical date collection screen:

```json
{
  "id": "BOOKING_DATES",
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "TextHeading",
        "text": "When would you like to book?"
      },
      {
        "type": "CalendarPicker",
        "name": "check_in",
        "label": "Check-in Date",
        "mode": "single",
        "min-date": "2024-02-01",
        "required": true
      },
      {
        "type": "CalendarPicker",
        "name": "check_out",
        "label": "Check-out Date",
        "mode": "single",
        "min-date": "2024-02-02",
        "required": true
      },
      {
        "type": "Footer",
        "label": "Continue",
        "on-click-action": {
          "action": "data_exchange",
          "payload": {
            "check_in": "${form.check_in}",
            "check_out": "${form.check_out}"
          }
        }
      }
    ]
  }
}
```

---

## Dynamic Date Constraints

Min/max dates from server data:

```json
{
  "id": "APPOINTMENT",
  "data": {
    "type": "object",
    "properties": {
      "available_from": {
        "type": "string",
        "__example__": "2024-02-01"
      },
      "available_until": {
        "type": "string",
        "__example__": "2024-02-29"
      }
    }
  },
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "DatePicker",
        "name": "appointment",
        "label": "Select Date",
        "min-date": "${data.available_from}",
        "max-date": "${data.available_until}"
      }
    ]
  }
}
```

Server provides available date range, DatePicker restricts to those dates.

---

## Server-Side Date Validation

Always validate dates server-side:

```python
from datetime import datetime

def validate_dates(check_in: str, check_out: str):
    ci = datetime.fromisoformat(check_in)
    co = datetime.fromisoformat(check_out)

    # Check-out must be after check-in
    if co <= ci:
        return False, "Check-out must be after check-in"

    # At least 1 day stay
    days = (co - ci).days
    if days < 1:
        return False, "Minimum 1 night stay required"

    # Not too far in future
    today = datetime.now().date()
    if ci.date() > today.replace(year=today.year + 1):
        return False, "Cannot book more than 1 year in advance"

    return True, None
```

---

## Time Component Notes

Currently, no dedicated time picker in Flow JSON. For time selection:
- Use TextInput with `input-type: "text"` and pattern validation
- Use Dropdown with time options (e.g., "09:00 AM", "09:30 AM")
- Request via server endpoint and handle accordingly

Example time selection via Dropdown:

```json
{
  "type": "Dropdown",
  "name": "appointment_time",
  "label": "Time Slot",
  "data-source": {
    "type": "dynamic",
    "values": "${data.available_times}"
  }
}
```

Server provides: `["09:00 AM", "09:30 AM", "10:00 AM", ...]`

---

## Date Picker Best Practices

1. **Set appropriate date ranges** - Don't allow dates that don't make sense
2. **Use CalendarPicker for ranges** - Better UX than two separate DatePickers
3. **Validate server-side** - Never trust client dates alone
4. **Format dates for display** - Show user-friendly format in confirmations
5. **Handle timezones carefully** - Users are in different zones
6. **Don't require future dates unnecessarily** - Allow today by default
7. **Use clear labels** - "Check-in Date" not "Date"
8. **Set init-value when appropriate** - Pre-populate today for near-future bookings
9. **Consider date ranges for comparison** - Compare check-in and check-out dates
10. **Test with edge dates** - Leap years, month boundaries, year boundaries

---

## Common Patterns

### Hotel Booking Flow

```json
{
  "id": "BOOKING",
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "CalendarPicker",
        "name": "dates",
        "label": "Select Dates",
        "mode": "range",
        "min-date": "${data.check_in_min}",
        "max-date": "${data.check_in_max}",
        "required": true
      },
      {
        "type": "Footer",
        "label": "Search",
        "on-click-action": {
          "action": "data_exchange",
          "payload": {
            "check_in": "${form.dates.start}",
            "check_out": "${form.dates.end}"
          }
        }
      }
    ]
  }
}
```

---

## Next Steps

- Learn **media components** in `07-media-components.md`
- Learn **conditional logic** in `10-conditional-logic.md`
- Learn **actions** in `13-actions.md`
