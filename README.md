# JR Carpet Care — website demo

Redesign demo for a Gold Coast carpet cleaning business.

`index.html` is the whole site in one file. Images and brand fonts are built in, so it can be deployed straight to Vercel, Netlify or GitHub Pages.

## Stock videos (add before deploying)

The hero and the "How a JR clean works" section play videos from `videos/`. Without them the page shows the brand photos instead.

```powershell
curl.exe -L -o videos\hero.mp4 "https://www.pexels.com/download/video/4201960/"
curl.exe -L -o videos\process.mp4 "https://www.pexels.com/download/video/4201927/"
```

Free Pexels clips: [steam cleaning](https://www.pexels.com/video/housework-carpet-living-room-steam-4201960/) and [carpet sprayer](https://www.pexels.com/video/carpet-sprayer-air-living-room-4201927/).

## Editing

- Prices, time slots, closed days and suburbs live in the `CFG` block near the top of the script in `source/template.html`.
- Edit `source/template.html`, then rebuild `index.html`:

```bash
cd source && python build.py
```

## Notes

- The prices are sample values. Replace them with the real rates before launch.
- Booking requests are sent by WhatsApp or email. There is no database yet.
- The review cards are placeholders. Paste in real Google reviews.
