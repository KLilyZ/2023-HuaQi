<template>
  <div class="wrapper">
    <VueScrollbar>
      <div class="content">
        <p>Scrollable content goes here
        Scrollable content goes here
        Scrollable content goes here
        Scrollable content goes here</p>
      </div>
    </VueScrollbar>
  </div>
</template>

<script>
import VueScrollbar from 'vue3-scrollbar'

export default {
  name:'MyScroll',
  components: {
    VueScrollbar
  }
}
</script>

<style>
.wrapper {
  height: 300px;
}

.content {
  height: 500px;
}
</style>
