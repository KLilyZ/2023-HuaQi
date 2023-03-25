<template>
  <div class="image-container" :style="imageStyle">
    <img :src="imageUrl" alt="Image">
  </div>
</template>

<script>
export default {
  data() {
    return {
      // imageUrl: '../assets/logo.png', // 图片链接
      imageWidth: 0, // 图片实际宽度
      imageHeight: 0, // 图片实际高度
      containerWidth: 0, // 图片容器宽度
      containerHeight: 0 // 图片容器高度
    };
  },
  props:{
    imageUrl:String
  },
  computed: {
    imageStyle() {
      // 计算图片样式
      if (this.imageWidth > 0 && this.imageHeight > 0 && this.containerWidth > 0 && this.containerHeight > 0) {
        let scale = Math.min(this.containerWidth / this.imageWidth, this.containerHeight / this.imageHeight);
        let width = Math.round(this.imageWidth * scale);
        let height = Math.round(this.imageHeight * scale);
        let top = Math.round((this.containerHeight - height) / 2);
        let left = Math.round((this.containerWidth - width) / 2);
        return {
          width: `${width}px`,
          height:  `${height}px `,
          position: 'absolute',
          top:  `${top}px` ,
          left: `${left}px`
        };
      } else {
        return {};
      }
    }
  },
  mounted() {
    // 图片加载完成后获取图片尺寸和容器尺寸
    let img = new Image();
    img.src = this.imageUrl;
    console.log(img.src)
    img.onload = () => {
      this.imageWidth = img.width;
      this.imageHeight = img.height;
      let container = this.$el.querySelector('.image-container');
      this.containerWidth = container.offsetWidth;
      this.containerHeight = container.offsetHeight;
    };
  }
};
</script>

<style>
.image-container {
  position: relative;
  margin: 0;
  width: 50%;
  height: 50%;
  /*background: #1b1b1b;*/
  overflow: hidden;
  display: flex;
  justify-content: center;
}
.image-container img {
  /*display: block;*/
  width: 70%;
  height: 70%;
  padding: 0;
  object-fit: fill;
}
</style>
