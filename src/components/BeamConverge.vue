<template>
  <canvas ref="canvasEl" class="beam-canvas" />
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const canvasEl = ref<HTMLCanvasElement>()
let animId = 0
let resizeObs: ResizeObserver

interface Beam {
  angle: number      // radian from center outward (beam comes FROM this angle)
  speed: number      // how fast the pulse travels (px/s normalised)
  phase: number      // time offset so beams don't all pulse in sync
  width: number      // stroke width at origin
  hue: number        // HSL hue for colour variation
}

const NUM_BEAMS = 14
const beams: Beam[] = Array.from({ length: NUM_BEAMS }, (_, i) => ({
  angle: (i / NUM_BEAMS) * Math.PI * 2,
  speed: 0.55 + Math.random() * 0.35,
  phase: Math.random() * Math.PI * 2,
  width: 1.5 + Math.random() * 2.5,
  hue: 200 + Math.random() * 80, // blue-cyan-violet range
}))

onMounted(() => {
  const canvas = canvasEl.value!
  const ctx = canvas.getContext('2d')!

  let w = 0, h = 0

  const resize = () => {
    w = canvas.width = canvas.offsetWidth * devicePixelRatio
    h = canvas.height = canvas.offsetHeight * devicePixelRatio
    ctx.scale(devicePixelRatio, devicePixelRatio)
  }

  resizeObs = new ResizeObserver(resize)
  resizeObs.observe(canvas)
  resize()

  const start = performance.now()

  const frame = () => {
    const now = (performance.now() - start) / 1000
    const W = canvas.offsetWidth
    const H = canvas.offsetHeight
    const cx = W / 2
    const cy = H / 2
    // max beam length — reach the canvas corners
    const maxLen = Math.hypot(W, H) * 0.6

    ctx.clearRect(0, 0, W, H)

    for (const beam of beams) {
      // pulse: a bright band that travels from far edge → center
      // t in [0,1] represents where the pulse head is (1 = at center)
      const raw = ((now * beam.speed + beam.phase) % (Math.PI * 2)) / (Math.PI * 2)
      const t = raw // 0→far, 1→center (we reverse: pulse HEAD approaches center)

      // outermost start point of the beam
      const startX = cx + Math.cos(beam.angle) * maxLen
      const startY = cy + Math.sin(beam.angle) * maxLen

      // The pulse head position along the beam (1-t because 0=far, 1=center)
      const headFrac = 1 - t  // distance from center as fraction of maxLen
      const headX = cx + Math.cos(beam.angle) * maxLen * headFrac
      const headY = cy + Math.sin(beam.angle) * maxLen * headFrac

      // --- dim base beam (full length, very faint) ---
      const baseGrad = ctx.createLinearGradient(startX, startY, cx, cy)
      baseGrad.addColorStop(0, `hsla(${beam.hue}, 90%, 70%, 0)`)
      baseGrad.addColorStop(0.5, `hsla(${beam.hue}, 90%, 70%, 0.04)`)
      baseGrad.addColorStop(1, `hsla(${beam.hue}, 90%, 70%, 0.12)`)
      ctx.save()
      ctx.strokeStyle = baseGrad
      ctx.lineWidth = beam.width
      ctx.beginPath()
      ctx.moveTo(startX, startY)
      ctx.lineTo(cx, cy)
      ctx.stroke()
      ctx.restore()

      // --- bright pulse segment trailing behind the head ---
      const tailLen = maxLen * 0.28  // how long the bright pulse trail is
      const tailFrac = headFrac + tailLen / maxLen
      const tailX = cx + Math.cos(beam.angle) * maxLen * Math.min(tailFrac, 1)
      const tailY = cy + Math.sin(beam.angle) * maxLen * Math.min(tailFrac, 1)

      const pulseGrad = ctx.createLinearGradient(tailX, tailY, headX, headY)
      pulseGrad.addColorStop(0, `hsla(${beam.hue}, 100%, 80%, 0)`)
      pulseGrad.addColorStop(0.6, `hsla(${beam.hue}, 100%, 80%, 0.55)`)
      pulseGrad.addColorStop(1, `hsla(${beam.hue}, 100%, 95%, 0.95)`)
      ctx.save()
      ctx.strokeStyle = pulseGrad
      ctx.lineWidth = beam.width * 1.6
      ctx.lineCap = 'round'
      // glow pass
      ctx.filter = `blur(${beam.width * 2.5}px)`
      ctx.beginPath()
      ctx.moveTo(tailX, tailY)
      ctx.lineTo(headX, headY)
      ctx.stroke()
      // sharp core
      ctx.filter = 'none'
      ctx.lineWidth = beam.width * 0.7
      ctx.beginPath()
      ctx.moveTo(tailX, tailY)
      ctx.lineTo(headX, headY)
      ctx.stroke()
      ctx.restore()
    }

    // --- center glow point ---
    const centerGlow = ctx.createRadialGradient(cx, cy, 0, cx, cy, 60)
    centerGlow.addColorStop(0, 'rgba(160, 200, 255, 0.90)')
    centerGlow.addColorStop(0.2, 'rgba(100, 160, 255, 0.55)')
    centerGlow.addColorStop(0.6, 'rgba(80, 120, 220, 0.20)')
    centerGlow.addColorStop(1, 'rgba(0,0,0,0)')
    ctx.save()
    ctx.filter = 'blur(8px)'
    ctx.fillStyle = centerGlow
    ctx.beginPath()
    ctx.arc(cx, cy, 60, 0, Math.PI * 2)
    ctx.fill()
    // bright white core
    ctx.filter = 'none'
    const coreGlow = ctx.createRadialGradient(cx, cy, 0, cx, cy, 10)
    coreGlow.addColorStop(0, 'rgba(255,255,255,1)')
    coreGlow.addColorStop(0.4, 'rgba(200,220,255,0.8)')
    coreGlow.addColorStop(1, 'rgba(100,150,255,0)')
    ctx.fillStyle = coreGlow
    ctx.beginPath()
    ctx.arc(cx, cy, 10, 0, Math.PI * 2)
    ctx.fill()
    ctx.restore()

    animId = requestAnimationFrame(frame)
  }

  animId = requestAnimationFrame(frame)
})

onUnmounted(() => {
  cancelAnimationFrame(animId)
  resizeObs?.disconnect()
})
</script>

<style scoped>
.beam-canvas {
  display: block;
  width: 100%;
  height: 100%;
  background: transparent;
}
</style>
