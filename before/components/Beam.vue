<template>
  <svg
    class="absolute top-0 left-0 w-full h-full"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <!-- 复刻原版：多段不连续的网格线，linearGradient 动画扫过 -->

    <path v-for="(beam, i) in BEAMS" :key="i"
      :d="beam.d"
      :stroke="`url(#g${i})`"
      stroke-width="1.5"
    />

    <defs>
      <linearGradient v-for="(grad, i) in grads" :key="`g${i}`"
        :id="`g${i}`"
        :x1="grad.x1" :y1="grad.y1" :x2="grad.x2" :y2="grad.y2"
      >
        <stop :stop-color="BEAMS[i].colors[0]" stop-opacity="0" />
        <stop :stop-color="BEAMS[i].colors[1]" />
        <stop offset="0.325" :stop-color="BEAMS[i].colors[2]" />
        <stop offset="1" :stop-color="BEAMS[i].colors[3]" stop-opacity="0" />
      </linearGradient>
    </defs>
  </svg>
</template>

<script setup lang="ts">
import { reactive, onMounted, onUnmounted } from 'vue'

// 8 条光束，延迟分布在整个周期内，保证连续但不拥挤
const BEAMS = [
  { d: 'M96 64h64M64 64h64m64 64h64m-32 0h64m-32 64h64M192 128V64m128 160V128',       delay: 0,    colors: ['#18CCFC', '#18CCFC', '#6344F5', '#AE48FF'] },
  { d: 'M448 96h64M416 96h64m64 64h64m-32 0h64m-32 64h64M544 160V96m128 160V160',     delay: 1100, colors: ['#00FF88', '#00FF88', '#00D9FF', '#00B4D8'] },
  { d: 'M768 32h64M736 32h64m64 64h64m-32 0h64m-32 64h64M864 96V32m128 160V96',       delay: 2200, colors: ['#18CCFC', '#18CCFC', '#6344F5', '#AE48FF'] },
  { d: 'M192 320h64M160 320h64m64 64h64m-32 0h64m-32 64h64M288 384V320m128 160V384',  delay: 3400, colors: ['#FF006E', '#FF006E', '#8338EC', '#3A86FF'] },
  { d: 'M576 256h64M544 256h64m64 64h64m-32 0h64m-32 64h64M672 320V256m128 160V320',  delay: 4500, colors: ['#FFD60A', '#FFD60A', '#FCA311', '#F48C06'] },
  { d: 'M128 480h64M96 480h64m64 64h64m-32 0h64m-32 64h64M224 544V480m128 160V544',   delay: 5600, colors: ['#18CCFC', '#18CCFC', '#6344F5', '#AE48FF'] },
  { d: 'M704 416h64M672 416h64m64 64h64m-32 0h64m-32 64h64M800 480V416m128 160V480',  delay: 6800, colors: ['#F72585', '#F72585', '#B5179E', '#7209B7'] },
  { d: 'M288 192h64M256 192h64m64 64h64m-32 0h64m-32 64h64M384 256V192m128 160V256',  delay: 7900, colors: ['#06FFA5', '#06FFA5', '#00D9A3', '#00B48D'] },
]

// 渐变动画参数：从上往下（FROM 在上方，TO 在下方）
const FROM = { x1: '0%',  x2: '10%', y1: '-40%', y2: '-20%' }
const TO   = { x1: '40%', x2: '50%', y1: '160%', y2: '180%' }

const DURATION = 5000      // 持续时间再长一点
const REPEAT_DELAY = 4000  // 原版2秒 × 2

const grads = reactive(
  BEAMS.map(() => ({ ...FROM }))
)

let rafId: number
let startTime: number | null = null

function parsePct(v: string) {
  return parseFloat(v)
}

function lerp(a: number, b: number, t: number) {
  return a + (b - a) * t
}

function tick(now: number) {
  if (startTime === null) startTime = now

  BEAMS.forEach((beam, i) => {
    const totalCycle = DURATION + REPEAT_DELAY
    const elapsed = (now - startTime! - beam.delay + totalCycle * 100) % totalCycle
    const t = Math.max(0, Math.min(1, elapsed / DURATION))

    // 线性插值，从 FROM 到 TO
    grads[i].x1 = lerp(parsePct(FROM.x1), parsePct(TO.x1), t) + '%'
    grads[i].x2 = lerp(parsePct(FROM.x2), parsePct(TO.x2), t) + '%'
    grads[i].y1 = lerp(parsePct(FROM.y1), parsePct(TO.y1), t) + '%'
    grads[i].y2 = lerp(parsePct(FROM.y2), parsePct(TO.y2), t) + '%'
  })

  rafId = requestAnimationFrame(tick)
}

onMounted(() => { rafId = requestAnimationFrame(tick) })
onUnmounted(() => { cancelAnimationFrame(rafId) })
</script>
