<template>
  <canvas ref="canvasEl" class="aurora-canvas" />
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const canvasEl = ref<HTMLCanvasElement>()
let animId = 0

interface Ribbon {
  // Y positions as fraction of height for 4 control columns (x fixed at -10%, 25%, 65%, 110%)
  yBase: number[]
  // Oscillation: phase offset and amplitude (fraction of height) per control point
  phase: number[]
  amp:   number[]
  freq:  number[]
  // Visual
  colors: [string, string, string]
  strokeWidth: number
  alpha: number
}

const RIBBONS: Ribbon[] = [
  {
    yBase:  [0.08,  0.00,  0.12,  0.06],
    phase:  [0.0,   1.3,   2.7,   4.1],
    amp:    [0.055, 0.090, 0.070, 0.045],
    freq:   [0.38,  0.46,  0.32,  0.42],
    colors: ['#6d28d9', '#c026d3', '#7c3aed'],
    strokeWidth: 90,
    alpha: 0.72,
  },
  {
    yBase:  [0.04,  -0.03, 0.07,  0.02],
    phase:  [0.8,   2.1,   3.5,   5.0],
    amp:    [0.040, 0.075, 0.055, 0.035],
    freq:   [0.50,  0.36,  0.44,  0.30],
    colors: ['#4f46e5', '#a855f7', '#6366f1'],
    strokeWidth: 55,
    alpha: 0.65,
  },
  {
    yBase:  [0.14,  0.08,  0.18,  0.12],
    phase:  [1.6,   3.0,   0.4,   1.9],
    amp:    [0.060, 0.095, 0.080, 0.050],
    freq:   [0.42,  0.54,  0.38,  0.48],
    colors: ['#be185d', '#f43f5e', '#e879f9'],
    strokeWidth: 70,
    alpha: 0.60,
  },
  {
    yBase:  [-0.02, 0.05,  0.01,  -0.04],
    phase:  [2.4,   3.8,   5.2,   0.6],
    amp:    [0.035, 0.065, 0.045, 0.030],
    freq:   [0.55,  0.40,  0.50,  0.35],
    colors: ['#0284c7', '#06b6d4', '#818cf8'],
    strokeWidth: 40,
    alpha: 0.75,
  },
  {
    yBase:  [0.10,  0.04,  0.14,  0.09],
    phase:  [3.2,   4.6,   1.0,   2.5],
    amp:    [0.045, 0.080, 0.060, 0.040],
    freq:   [0.34,  0.48,  0.42,  0.56],
    colors: ['#7e22ce', '#db2777', '#9333ea'],
    strokeWidth: 30,
    alpha: 0.80,
  },
  {
    yBase:  [0.18,  0.12,  0.22,  0.16],
    phase:  [4.0,   5.4,   1.8,   3.3],
    amp:    [0.050, 0.085, 0.065, 0.042],
    freq:   [0.46,  0.38,  0.52,  0.44],
    colors: ['#1d4ed8', '#7c3aed', '#2563eb'],
    strokeWidth: 50,
    alpha: 0.55,
  },
]

// Control point X positions (as fraction of canvas width)
const XS = [-0.10, 0.28, 0.68, 1.10]

function drawRibbon(
  ctx: CanvasRenderingContext2D,
  w: number, h: number,
  r: Ribbon,
  t: number,
) {
  const xs = XS.map(f => f * w)
  const ys = r.yBase.map((yf, i) =>
    (yf + Math.sin(t * r.freq[i] + r.phase[i]) * r.amp[i]) * h
  )

  // Glow passes: wide blurry → medium → thin sharp core
  const passes = [
    { widthMult: 5.0, alphaMult: 0.10, blur: 48 },
    { widthMult: 3.0, alphaMult: 0.18, blur: 24 },
    { widthMult: 1.8, alphaMult: 0.35, blur: 10 },
    { widthMult: 0.9, alphaMult: 0.70, blur: 4  },
    { widthMult: 0.3, alphaMult: 1.00, blur: 0  },
  ]

  for (const pass of passes) {
    ctx.save()
    if (pass.blur > 0) ctx.filter = `blur(${pass.blur}px)`
    ctx.globalAlpha = r.alpha * pass.alphaMult
    ctx.lineWidth = r.strokeWidth * pass.widthMult
    ctx.lineCap = 'round'

    const grad = ctx.createLinearGradient(xs[0], ys[0], xs[3], ys[3])
    grad.addColorStop(0.0, r.colors[0])
    grad.addColorStop(0.5, r.colors[1])
    grad.addColorStop(1.0, r.colors[2])
    ctx.strokeStyle = grad

    ctx.beginPath()
    ctx.moveTo(xs[0], ys[0])
    ctx.bezierCurveTo(xs[1], ys[1], xs[2], ys[2], xs[3], ys[3])
    ctx.stroke()
    ctx.restore()
  }
}

onMounted(() => {
  const canvas = canvasEl.value!
  const ctx = canvas.getContext('2d')!
  let w = 0, h = 0

  const resize = () => {
    w = canvas.width  = window.innerWidth
    h = canvas.height = window.innerHeight
  }
  resize()

  window.addEventListener('resize', resize)
  const ro = new ResizeObserver(resize)
  ro.observe(document.documentElement)

  const start = performance.now()

  const frame = () => {
    const t = (performance.now() - start) / 1000
    ctx.clearRect(0, 0, w, h)

    // Draw back-to-front for correct layering
    for (const ribbon of RIBBONS) {
      drawRibbon(ctx, w, h, ribbon, t)
    }

    animId = requestAnimationFrame(frame)
  }
  animId = requestAnimationFrame(frame)

  onUnmounted(() => {
    cancelAnimationFrame(animId)
    window.removeEventListener('resize', resize)
    ro.disconnect()
  })
})
</script>

<style scoped>
.aurora-canvas {
  display: block;
  width: 100%;
  height: 100%;
  pointer-events: none;
}
</style>
