# Deployment & Launch Guide

## 1. Cloudflare Transition Strategy
**Your Question**: *"Can I ask her to invite me and then I point the thing at our domain?"*
**Answer**: **YES**. This is the most professional and secure workflow.

### Step-by-Step
1.  **Request Access**: Ask the client to invite you to her Cloudflare account (User Icon > Account Members > Invite). Request **Administrator** or **DNS** privileges.
2.  **Accept Invite**: You will receive an email. Create/Login to your Cloudflare account to accept.
3.  **Access Domain**: You should now see `thewallstreetcoach.com` in your dashboard.

## 2. Hosting & DNS Updates
Before updating Cloudflare, you need to deploy the files.

### Option A: Netlify / Vercel (Recommended)
1.  Deploy the `Antigravity` folder.
2.  Ensure `_redirects` is in the publish directory.
3.  Add `thewallstreetcoach.com` in the domain settings of the host.
4.  **Get DNS Values**: The host will provide an A Record (IP) or CNAME.
5.  **Update Cloudflare**:
    *   Go to **DNS** in Cloudflare.
    *   Replace the existing `@` (A record) and `www` (CNAME) with the new values provided by Netlify/Vercel.

### Option B: Cloudflare Pages
1.  Since DNS is already on Cloudflare, you can host purely within Cloudflare.
2.  Go to **Workers & Pages** > Create Application > Upload Assets.
3.  Upload the `Antigravity` folder.
4.  Set up the custom domain linkage internally (instant update).

### Option C: Standard Hosting (cPanel/FTP)
1.  Upload all files via FTP.
2.  **Crucial**: Ensure `.htaccess` is uploaded to the root directory (this handles the redirects on these servers).
3.  Update Cloudflare A Record to point to the new server IP.

## 3. SEO Preservation Assets
We have generated all necessary files to preserve rankings. Ensure the correct file is present on your host:

| Hosting Platform | File Needed | Status |
| :--- | :--- | :--- |
| **Netlify / CF Pages** | `_redirects` | ✅ Created |
| **Generic / cPanel** | `.htaccess` | ✅ Created |
| **Vercel** | `vercel.json` | *Uses _redirects often, or convert* |
| **Manual / Other** | `redirects.csv` | ✅ Created |

## 4. Verification
After switching DNS:
1.  **Test Redirects**:
    *   Old Link: `thewallstreetcoach.com/trader-coaching/` -> New: `/coaching.html`
    *   Old Blog: `thewallstreetcoach.com/blog/2022/...` -> New: `/episodes/...`
2.  **Test Privacy Policy**: Ensure the new `privacy-policy.html` loads.
