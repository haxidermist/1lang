# GitHub Pages Setup Guide

To enable the browser-readable ebook, you need to activate GitHub Pages for your repository.

## Quick Setup (2 minutes)

1. **Go to your repository on GitHub**
   - Visit: https://github.com/haxidermist/1lang

2. **Open Settings**
   - Click the "Settings" tab (gear icon)

3. **Navigate to Pages**
   - In the left sidebar, click "Pages" under "Code and automation"

4. **Configure Source**
   - Under "Build and deployment"
   - Source: Select "Deploy from a branch"
   - Branch: Select "main"
   - Folder: Select "/docs"
   - Click "Save"

5. **Wait for Deployment**
   - GitHub will build and deploy your site
   - This takes 1-2 minutes
   - You'll see a green checkmark when ready

6. **Access Your Book**
   - Main site: https://haxidermist.github.io/1lang/
   - eBook: https://haxidermist.github.io/1lang/ebook/

## What Gets Deployed

### Landing Page
**URL:** https://haxidermist.github.io/1lang/

Beautiful landing page featuring:
- The 1 language overview
- Direct link to the ebook
- Link to GitHub repository
- Key features showcase

### Complete eBook
**URL:** https://haxidermist.github.io/1lang/ebook/

Full book with:
- All 6 chapters + appendix
- Professional styling
- Interactive table of contents
- Chapter navigation
- Code syntax highlighting
- Responsive design
- Print-friendly layout

## Verification

After enabling GitHub Pages:

1. **Check Actions Tab**
   - Click "Actions" in your repository
   - You should see "pages build and deployment" workflow
   - Wait for green checkmark

2. **Visit the Site**
   - Go to https://haxidermist.github.io/1lang/ebook/
   - The book should load with proper formatting
   - All chapters should be accessible

3. **Test Navigation**
   - Click on chapter links in table of contents
   - Use navigation buttons between chapters
   - Try the back-to-top button

## Troubleshooting

### Site Not Loading?

1. **Check Repository Settings**
   - Verify Pages is enabled
   - Ensure source is "main" branch, "/docs" folder

2. **Check Actions**
   - Go to Actions tab
   - Look for failed deployments
   - Click on failed action for details

3. **Wait Longer**
   - First deployment can take 5-10 minutes
   - Subsequent updates are faster (1-2 minutes)

### 404 Errors?

1. **Verify Files Exist**
   - Check that `docs/` folder exists in main branch
   - Verify `docs/index.html` and `docs/ebook/index.html` are present

2. **Check Paths**
   - GitHub Pages URLs are case-sensitive
   - Ensure paths match exactly

### CSS Not Loading?

1. **Check Browser Console**
   - Open developer tools (F12)
   - Look for errors in console
   - Verify CSS files are loading

2. **Clear Cache**
   - Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)

## Updating the Book

When you make changes to the ebook:

1. **Edit Files**
   - Modify markdown files in `ebook/` directory
   - Changes automatically sync to `docs/ebook/`

2. **Commit and Push**
   ```bash
   git add .
   git commit -m "Update ebook chapter X"
   git push
   ```

3. **Wait for Deployment**
   - GitHub automatically rebuilds the site
   - Takes 1-2 minutes
   - Check Actions tab for progress

4. **Verify Changes**
   - Visit the live site
   - Hard refresh to see updates
   - Check that changes appear correctly

## Custom Domain (Optional)

To use a custom domain like `1lang.com`:

1. **Add Domain**
   - In Pages settings, add your custom domain
   - Example: `book.1lang.com`

2. **Configure DNS**
   - Add CNAME record pointing to `haxidermist.github.io`
   - Or A records pointing to GitHub's IPs

3. **Enable HTTPS**
   - GitHub Pages automatically provides SSL certificate
   - Check "Enforce HTTPS" in settings

## Analytics (Optional)

To track visitors:

1. **Google Analytics**
   - Add tracking code to `docs/ebook/index.html`
   - Insert before `</head>` tag

2. **GitHub Insights**
   - Go to repository Insights > Traffic
   - View page views and visitors

## Sharing the Book

Once deployed, share these links:

- **Landing Page:** https://haxidermist.github.io/1lang/
- **Complete Book:** https://haxidermist.github.io/1lang/ebook/
- **Direct Chapter Links:**
  - Preface: https://haxidermist.github.io/1lang/ebook/#chapter-0
  - Chapter 1: https://haxidermist.github.io/1lang/ebook/#chapter-1
  - Chapter 2: https://haxidermist.github.io/1lang/ebook/#chapter-2
  - etc.

## Support

If you encounter issues:

1. Check GitHub Status: https://www.githubstatus.com/
2. Review GitHub Pages docs: https://docs.github.com/en/pages
3. Check repository Actions for build errors

---

**That's it! Your ebook is now live and browser-readable! 📖**

Enjoy sharing "The 1 Programming Language" with the world!
