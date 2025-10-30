# Media Components

Components for displaying and uploading images and documents.

---

## Image

Display static images on a screen.

**Properties:**
- `src` - Image URL (required, must be HTTPS)
- `scale-type` - How to scale image: `center-crop` (default) or `fill`
- `aspect-ratio` - Optional ratio (e.g., `1:1`, `16:9`)

### Basic Image

```json
{
  "type": "Image",
  "src": "https://example.com/product.jpg"
}
```

### Image with Aspect Ratio

```json
{
  "type": "Image",
  "src": "https://example.com/banner.jpg",
  "scale-type": "fill",
  "aspect-ratio": "16:9"
}
```

### Image Specifications

- Format: JPEG, PNG, WebP
- Max size: 300KB recommended, hard limit varies
- HTTPS required (no HTTP)
- Recommended dimensions: 600x400px or larger
- Scale types:
  - `center-crop` - Crop to fit, maintaining aspect ratio
  - `fill` - Stretch to fill space

### Image Component Limits

- Maximum 3 images per screen
- Most common: 1-2 images per screen
- Spacing managed by layout

### Image URLs

Ensure URLs are:
- HTTPS only
- Publicly accessible (no authentication required)
- Stable (CDN-backed preferred)
- Fast loading (optimized for mobile)

```json
{
  "type": "Image",
  "src": "https://cdn.example.com/images/product-123.jpg"
}
```

---

## PhotoPicker (v5.0+)

Allow users to upload photos from device.

**Properties:**
- `name` - Field identifier (required)
- `label` - Button label (optional, default: "Add Photo")
- `required` - Must upload photo (default: false)

### Basic PhotoPicker

```json
{
  "type": "PhotoPicker",
  "name": "user_photo",
  "label": "Upload Your Photo"
}
```

### PhotoPicker in Form

```json
{
  "type": "SingleColumnLayout",
  "children": [
    {
      "type": "TextHeading",
      "text": "Submit Your Photo"
    },
    {
      "type": "PhotoPicker",
      "name": "submission_photo",
      "label": "Choose Photo",
      "required": true
    },
    {
      "type": "Footer",
      "label": "Upload"
    }
  ]
}
```

### Form Value

Uploaded photo reference (actual image data sent in separate media upload):

```json
${form.user_photo}  // Reference to uploaded media
```

### Photo Upload Details

- Format: JPEG, PNG
- Max size per photo: ~20MB
- Separate media upload endpoint (not in Flow JSON)
- Server receives media metadata, not inline data

---

## DocumentPicker (v5.0+)

Allow users to upload documents (PDF, Word, etc.).

**Properties:**
- `name` - Field identifier (required)
- `label` - Button label (optional, default: "Add Document")
- `required` - Must upload document (default: false)

### Basic DocumentPicker

```json
{
  "type": "DocumentPicker",
  "name": "contract",
  "label": "Upload Contract"
}
```

### Multiple Document Uploads

```json
{
  "type": "SingleColumnLayout",
  "children": [
    {
      "type": "TextHeading",
      "text": "Supporting Documents"
    },
    {
      "type": "DocumentPicker",
      "name": "id_document",
      "label": "ID or Passport",
      "required": true
    },
    {
      "type": "DocumentPicker",
      "name": "proof_of_address",
      "label": "Proof of Address"
    },
    {
      "type": "Footer",
      "label": "Submit"
    }
  ]
}
```

### Document Types

Supported formats:
- PDF (.pdf)
- Microsoft Word (.doc, .docx)
- Microsoft Excel (.xls, .xlsx)
- Text (.txt)
- Others supported may vary

Max size per document: ~20MB

---

## ImageCarousel (v7.1+)

Slide through multiple images.

**Properties:**
- `images` - Array of image objects (1-3 images)
- `scale-type` - `center-crop` or `fill`
- `aspect-ratio` - Optional ratio

### ImageCarousel Example

```json
{
  "type": "ImageCarousel",
  "images": [
    {
      "src": "https://example.com/image1.jpg"
    },
    {
      "src": "https://example.com/image2.jpg"
    },
    {
      "src": "https://example.com/image3.jpg"
    }
  ],
  "aspect-ratio": "1:1",
  "scale-type": "fill"
}
```

### ImageCarousel Limits

- Minimum 1 image, maximum 3 images
- Maximum 2 ImageCarousel per screen
- Same image specifications as Image component

### Use Cases

- Product gallery
- Multiple photos of item
- Step-by-step visual guide
- Before/after comparisons

---

## Media Component Combinations

Typical screen with images and inputs:

```json
{
  "id": "PRODUCT_DETAILS",
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "ImageCarousel",
        "images": [
          { "src": "https://example.com/prod1.jpg" },
          { "src": "https://example.com/prod2.jpg" }
        ]
      },
      {
        "type": "TextHeading",
        "text": "Product Name"
      },
      {
        "type": "TextBody",
        "text": "Description of the product"
      },
      {
        "type": "Dropdown",
        "name": "size",
        "label": "Size",
        "data-source": {
          "type": "static",
          "values": ["S", "M", "L", "XL"]
        }
      },
      {
        "type": "Footer",
        "label": "Add to Cart"
      }
    ]
  }
}
```

---

## Image Specifications

### URL Requirements
- Must be HTTPS
- Must be publicly accessible
- Recommended CDN for fast delivery
- No redirects preferred
- Stable URLs (avoid temporary URLs)

### Image Dimensions
- Recommended: 600x400px or larger
- Aspect ratio: match `aspect-ratio` property
- DPI: 72+ for web
- Optimization: compress for mobile

### Image Hosting
Good options:
- AWS S3 + CloudFront
- Google Cloud Storage
- Azure Blob Storage
- CDN like Cloudflare, Akamai
- Dedicated image CDN like Imgix, Cloudinary

---

## Media Upload Flow

When user submits PhotoPicker or DocumentPicker:

1. **User selects file** on device
2. **Flow sends reference** to backend (not the file data)
3. **Server initiates media upload** via separate endpoint
4. **User uploads media** through WhatsApp infrastructure
5. **Server stores/processes media**
6. **Flow continues** to next screen

Requires coordination between Flow backend and media upload API.

---

## Image Best Practices

1. **Use HTTPS always** - No insecure HTTP
2. **Optimize file size** - Keep under 200KB
3. **Choose appropriate dimensions** - 600x400 minimum
4. **Match aspect ratio** - Set `aspect-ratio` if known
5. **Use descriptive URLs** - `product-123.jpg` not `IMG_0001.JPG`
6. **Cache appropriately** - Use CDN with long cache
7. **Test on mobile** - Verify load time and appearance
8. **Provide alt text** (in description) - Accessibility
9. **Use consistent styling** - Similar colors, borders, styling
10. **Compress before hosting** - Use ImageOptim, TinyPNG, etc.

---

## PhotoPicker/DocumentPicker Best Practices

1. **Only require when necessary** - Users may skip required uploads
2. **Provide clear instructions** - "Upload driver's license front side"
3. **Specify format requirements** - "PDF or image file"
4. **Set realistic file limits** - Inform users of constraints
5. **Handle upload failures gracefully** - Show retry option
6. **Validate file types server-side** - Never trust client
7. **Store securely** - Encrypt sensitive documents
8. **Comply with regulations** - GDPR, PII handling, data retention
9. **Consider compression** - Auto-compress large files if possible
10. **Test on poor connectivity** - Uploads may be slow

---

## ImageCarousel Best Practices

1. **Limit to 3 images max** - More is overwhelming
2. **Order logically** - Most important first
3. **Consistent aspect ratio** - All images same ratio
4. **Clear navigation** - Users understand they can swipe
5. **Don't auto-advance** - User-controlled
6. **Use for related content** - Gallery, not unrelated images
7. **Test on mobile** - Verify swipe works smoothly
8. **Compress all images** - Consistent load time
9. **Provide captions** (if needed) - TextCaption above carousel
10. **Avoid text in images** - Not accessible

---

## Next Steps

- Learn **rich text and navigation** in `08-rich-content.md` and `09-navigation-components.md`
- Learn **conditional logic** in `10-conditional-logic.md`
- Learn **actions** in `13-actions.md`
