<template>
  <div class="orbit-ring-wrap">
    <canvas ref="canvasEl" class="orbit-ring-canvas" />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const canvasEl = ref<HTMLCanvasElement>()
let animId = 0
let resizeHandler = () => {}

// (2,3) torus knot projected to 2D — produces oval with two side crossing-knots
function buildPoints(w: number, h: number, N = 700): [number, number][] {
  const pts: [number, number][] = []
  const cx = w / 2
  const cy = h / 2
  const R = 2.0
  const r = 0.68
  const norm = R + r
  const sx = Math.min(w * 0.40, h * 0.75)
  const sy = sx * 0.54

  for (let i = 0; i <= N; i++) {
    const t = (i / N) * Math.PI * 2
    const rr = R + r * Math.cos(3 * t)
    pts.push([
      cx + (sx * rr * Math.cos(2 * t)) / norm,
      cy + (sy * rr * Math.sin(2 * t)) / norm,
    ])
  }
  return pts
}

function buildLens(pts: [number, number][]): number[] {
  const lens = [0]
  for (let i = 1; i < pts.length; i++) {
    lens.push(
      lens[lens.length - 1] +
        Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]),
    )
  }
  return lens
}

onMounted(() => {
  const canvas = canvasEl.value!
  const ctx = canvas.getContext('2d')!

  let w = 0, h = 0
  let pts: [number, number][] = []
  let lens: number[] = []
  let total = 0

  resizeHandler = () => {
    w = canvas.width = canvas.offsetWidth
    h = canvas.height = canvas.offsetHeight
    pts = buildPoints(w, h)
    lens = buildLens(pts)
    total = lens[lens.length - 1]
  }

  resizeHandler()
  window.addEventListener('resize', resizeHandler)

  function drawSegment(
    offset: number,
    dashLen: number,
    color: string,
    lw: number,
    blur: number,
    alpha: number,
  ) {
    ctx.save()
    if (blur > 0) ctx.filter = `blur(${blur}px)`
    ctx.globalAlpha = alpha
    ctx.strokeStyle = color
    ctx.lineWidth = lw
    ctx.lineCap = 'round'
    ctx.lineJoin = 'round'
    ctx.beginPath()
    let penDown = false
    for (let i = 0; i < pts.length; i++) {
      const d = (lens[i] - offset + total) % total
      if (d <= dashLen) {
        if (!penDown) {
          ctx.moveTo(pts[i][0], pts[i][1])
          penDown = true
        } else {
          ctx.lineTo(pts[i][0], pts[i][1])
        }
      } else if (penDown) {
        ctx.stroke()
        ctx.beginPath()
        penDown = false
      }
    }
    if (penDown) ctx.stroke()
    ctx.restore()
  }

  const start = performance.now()

  const frame = () => {
    const t = (performance.now() - start) / 1000
    ctx.clearRect(0, 0, w, h)

    const offset = (t * total * 0.07) % total
    const dashLen = total * 0.62

    // Glow passes: widest/most blurred first → sharpest core last
    drawSegment(offset, dashLen, 'rgba(88,28,220,0.20)',  42, 50, 1)
    drawSegment(offset, dashLen, 'rgba(124,58,237,0.30)',  26, 30, 1)
    drawSegment(offset, dashLen, 'rgba(99,102,241,0.40)',  16, 18, 1)
    drawSegment(offset, dashLen, 'rgba(96,165,250,0.55)',   9, 10, 1)
    drawSegment(offset, dashLen, 'rgba(167,197,253,0.80)',  4,  5, 1)
    drawSegment(offset, dashLen, 'rgba(224,231,255,0.95)',  2,  0, 1)

    // Trailing tail fade (dim segment just behind the main dash)
    const tailOffset = (offset - total * 0.05 + total) % total
    drawSegment(tailOffset, total * 0.04, 'rgba(248,113,133,0.25)', 10, 15, 1)

    // Hot-spot at the leading edge — red-pink burst
    const hi = Math.round((offset / total) * (pts.length - 1)) % pts.length
    const [hx, hy] = pts[hi]
    ctx.save()
    ctx.filter = 'blur(16px)'
    const g = ctx.createRadialGradient(hx, hy, 0, hx, hy, 38)
    g.addColorStop(0, 'rgba(251, 113, 133, 0.95)')
    g.addColorStop(1, 'rgba(251, 113, 133, 0)')
    ctx.fillStyle = g
    ctx.beginPath()
    ctx.arc(hx, hy, 38, 0, Math.PI * 2)
    ctx.fill()
    ctx.restore()

    // Secondary hot-spot roughly opposite (the crossing knot on the other side)
    const hi2 = (hi + Math.floor(pts.length / 2)) % pts.length
    const [hx2, hy2] = pts[hi2]
    ctx.save()
    ctx.filter = 'blur(12px)'
    const g2 = ctx.createRadialGradient(hx2, hy2, 0, hx2, hy2, 24)
    g2.addColorStop(0, 'rgba(251, 113, 133, 0.50)')
    g2.addColorStop(1, 'rgba(251, 113, 133, 0)')
    ctx.fillStyle = g2
    ctx.beginPath()
    ctx.arc(hx2, hy2, 24, 0, Math.PI * 2)
    ctx.fill()
    ctx.restore()

    animId = requestAnimationFrame(frame)
  }

  animId = requestAnimationFrame(frame)
})

onUnmounted(() => {
  cancelAnimationFrame(animId)
  window.removeEventListener('resize', resizeHandler)
})
</script>

<style scoped>
.orbit-ring-wrap {
  position: absolute;
  inset: 0;
  pointer-events: none;
  /* dark purple background with subtle grid */
  background:
    linear-gradient(rgba(148, 163, 184, 0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(148, 163, 184, 0.04) 1px, transparent 1px),
    radial-gradient(ellipse 80% 60% at 50% 50%, #0d0829 0%, #060412 100%);
  background-size: 72px 72px, 72px 72px, 100% 100%;
}

.orbit-ring-canvas {
  display: block;
  width: 100%;
  height: 100%;
}
</style>
