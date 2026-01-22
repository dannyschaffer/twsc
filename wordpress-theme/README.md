# The Wall Street Coach - Custom WordPress Theme

## Installation
1.  Compress the `wordpress-theme` folder into a ZIP file (e.g., `twsc-theme.zip`).
2.  Go to your WordPress Admin -> **Appearance** -> **Themes** -> **Add New** -> **Upload Theme**.
3.  Upload the ZIP file and activate it.

## Development
- **front-page.php**: The content for the Homepage.
- **page-coaching.php**: Template for the "Coaching" page (Select "Coaching Page" in Page Attributes).
- **page-tpi.php**: Template for the "Assessment" page (Select "TPI Assessment Page" in Page Attributes).
- **page-about.php**: Template for the "About" page (Select "About Page" in Page Attributes).
- **page-podcast.php**: Template for the "Podcast" page.
- **page-resources.php**: Template for the "Resources" page.
- **page-book.php**: Template for the "Book Consultation" page.
- **page-download.php**: Template for the "Download" page.
- **page-library.php**: Template for the "Library" page (Success page for downloads).
- **page-privacy.php**: Template for the "Privacy Policy" page.
- **header.php**: The navigation and head section.
- **footer.php**: The footer and scripts.
- **functions.php**: Enqueues styles and scripts.
- **index.php**: Fallback template for standard pages (About, Privacy Policy, etc.).

## Migrating Content
- For pages like **About** or **Coaching**:
    - **Option A (Easy)**: Create a new Page in WordPress, paste the text into the editor. It will use `index.php`.
    - **Option B (Custom)**: If the design is complex, create a file named `page-coaching.php` (for slug 'coaching') and copy the HTML structure there, similar to `front-page.php`.
