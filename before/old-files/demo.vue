<template>
  <div class="flex items-center justify-center w-full h-full min-h-[400px] border border-gray-200 rounded-lg relative overflow-hidden">
    <div class="w-full h-[400px] dark:bg-grid-white/[0.05] bg-grid-black/[0.07]">
      <GridBeam>
        <div class="relative w-full h-full sm:pl-16 pt-28 pl-4 flex items-start justify-start">
          <div class="grid gap-2">
            <h1 class="sm:text-5xl text-4xl font-bold max-w-sm">
              能够提升转化率的亮点部分。
            </h1>
            <p class="text-neutral-500 max-w-lg">
              美丽的光束,顺便一提,这束光是我从Aceternity那里逆向工程过来的。
            </p>
          </div>
        </div>
      </GridBeam>
    </div>
  </div>
</template>

<script setup lang="ts">
import GridBeam from './GridBeam.vue'
</script>
