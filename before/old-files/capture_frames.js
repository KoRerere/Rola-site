// Capture frames of animation.html using Puppeteer's CDP Animation domain
// to step the animation deterministically (avoids real-time jitter and cache).
const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer');

const FILE = `file://${path.resolve(__dirname, 'animation.html')}`;
const OUT_DIR = path.resolve(__dirname, 'frames');
const FPS = 30;
const DURATION_S = 4.5; // total animation duration: ripple + pop + bob
const WIDTH = 590;
const HEIGHT = 522;
const SCALE = 2; // for retina-quality stills, gifski will downsize

(async () => {
  fs.rmSync(OUT_DIR, { recursive: true, force: true });
  fs.mkdirSync(OUT_DIR, { recursive: true });

  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-web-security'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: WIDTH, height: HEIGHT, deviceScaleFactor: SCALE });
  // Transparent background for the page itself.
  await page._client().send('Emulation.setDefaultBackgroundColorOverride', {
    color: { r: 0, g: 0, b: 0, a: 0 },
  });
  await page.goto(FILE, { waitUntil: 'networkidle0' });

  // Hide replay button + force transparent body.
  await page.addStyleTag({
    content: `.replay { display: none !important; } body, html, .stage { background: transparent !important; }`,
  });

  // Override animation timing to be controlled via a CSS variable so we can step it.
  // We freeze the animation to "paused" and use animation-delay (negative) trick to
  // sample at any instant. This way we can grab any frame deterministically.
  await page.evaluate(() => {
    const css = `
      .float-icon, .ripple-dot, .ripple-ring {
        animation-play-state: paused !important;
      }
    `;
    const style = document.createElement('style');
    style.id = '__freeze';
    style.textContent = css;
    document.head.appendChild(style);
  });

  const totalFrames = Math.round(FPS * DURATION_S);

  for (let i = 0; i < totalFrames; i++) {
    const t = i / FPS; // seconds
    // Apply a per-frame stylesheet that sets a strongly negative animation-delay so
    // the paused animation is sampled at time `t` from each element's own delay.
    await page.evaluate((tSec) => {
      let style = document.getElementById('__step');
      if (!style) {
        style = document.createElement('style');
        style.id = '__step';
        document.head.appendChild(style);
      }
      // For each icon: effective delay = original --delay - tSec, which advances time.
      // Easiest: enumerate all .float-icon and set their animation-delay inline.
      document.querySelectorAll('.float-icon').forEach((el) => {
        const cs = getComputedStyle(el);
        const origDelay = parseFloat(el.dataset.originalDelay ?? cs.getPropertyValue('--delay')) || 0;
        if (!el.dataset.originalDelay) el.dataset.originalDelay = String(origDelay);
        const bobPhase = parseFloat(cs.getPropertyValue('--bob-phase')) || 0;
        // pop runs 1.05s, then bob starts at origDelay+1.05+bobPhase
        const popDelay = origDelay - tSec;
        const bobDelay = origDelay + 1.05 + bobPhase - tSec;
        el.style.animationDelay = `${popDelay}s, ${bobDelay}s`;
      });
      // Ripple animations: dot at delay 0, rings at 0.05/0.18/0.31s.
      const rippleStarts = {
        '.ripple-dot': 0,
        '.ring-1': 0.05,
        '.ring-2': 0.18,
        '.ring-3': 0.31,
      };
      for (const [sel, start] of Object.entries(rippleStarts)) {
        document.querySelectorAll(sel).forEach((el) => {
          el.style.animationDelay = `${start - tSec}s`;
        });
      }
    }, t);

    const file = path.join(OUT_DIR, `frame_${String(i).padStart(4, '0')}.png`);
    await page.screenshot({
      path: file,
      clip: { x: 0, y: 0, width: WIDTH, height: HEIGHT },
      omitBackground: true,
    });
    if (i % 10 === 0) process.stdout.write(`  frame ${i}/${totalFrames}\r`);
  }
  console.log(`\nCaptured ${totalFrames} frames -> ${OUT_DIR}`);
  await browser.close();
})();
