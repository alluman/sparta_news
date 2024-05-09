<template>
  <div id="app">
    <MainNavbar />
    <router-view />
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
// import MainNavbar from './components/MainNavbar.vue';

export default {

  data() {
    return {
      message: ''
    }
  },
  mounted() {
    fetch('http://localhost:8000/api/test/')
      .then(response => response.json())
      .then(data => {
        this.message = data.message;
      })
      .catch(console.error);
  }
};
</script>

<style>
/* Global styles */
</style>
