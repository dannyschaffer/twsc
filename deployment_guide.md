# Deployment Instructions

## 1. Upload Static Episodes
1. Connect to your WP Engine site via SFTP.
2. Navigate to the **web root** folder (often `public` or matches your site name).
3. Upload/Unzip `episodes.zip` into this root folder.
   - It will create a folder: `/public/episodes/` containing the HTML files.
   - **Important:** Ensure you upload the `episodes` folder itself or unzip such that `episodes/` is created, not contents dumped in root. (The zip provided contains the folder).

## 2. Install the Theme
1. Log in to WordPress Admin.
2. Go to **Appearance > Themes > Add New > Upload Theme**.
3. Upload `twsc-theme.zip`.
4. **Activate** the theme.
   *Note: Uploading episodes first prevents dead links upon activation.*

## 3. Set Up Pages
The static pages (About, Podcast, Resources) are integrated into the Theme.
1. Go to **Pages > Add New** in WordPress.
2. Create pages for:
   - **Podcast** (Template: "Podcast Page")
   - **Resources** (Template: "Resources Page") - *Includes Live Coaching*
   - **About**, **Book**, **TPI** (Template usually auto-detected or select Default/Specific).
3. Publish them.

## 4. Import Redirects (Optional)
If migrating from an old blog structure:
1. In WP Engine Portal, go to **Redirect Rules**.
2. Import `redirects.csv` (included in package).

---

## How to Revert (Undo)
1. **Theme:** Activate your previous theme.
2. **Episodes:** Delete the `/episodes/` folder via SFTP.
3. **Redirects:** Delete the imported rules.
