<template>
  <div class="w-full h-full flex items-center justify-center p-8">
    <div class="flex items-center justify-center w-full max-w-6xl h-full min-h-[400px] border border-gray-200 dark:border-gray-700 rounded-lg relative overflow-hidden">
      <div class="w-full h-full dark:bg-grid-white/[0.05] bg-grid-black/[0.07]">
        <GridBeam />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import GridBeam from './components/GridBeam.vue'
</script>
