# JR Carpet Care — website demo

Redesign demo for a Gold Coast carpet cleaning business.

`index.html` is the whole site in one file. Images and brand fonts are built in, so it can be deployed straight to Vercel, Netlify or GitHub Pages.

## Stock videos

The hero and the "How a JR clean works" section stream free Pexels clips straight from the Pexels CDN, so nothing needs downloading: [steam cleaning](https://www.pexels.com/video/housework-carpet-living-room-steam-4201960/) and [carpet sprayer](https://www.pexels.com/video/carpet-sprayer-air-living-room-4201927/). Each video tries the 1080p file first and falls back to 1440p. If both fail to load, the brand photo shows instead. Videos only play while they're on screen.

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
