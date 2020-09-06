<template>
    <v-app>
        <v-app-bar color="white" app>
          <v-img
            class="mx-2"
            src="./assets/Quickline_Logo_RGB_positiv.png"
            max-height="40"
            max-width="80"
            contain
          ></v-img>
          <v-spacer></v-spacer>
          <v-icon class="pa-2" color="black">
            mdi-magnify
          </v-icon>
          <v-icon color="black">
            mdi-menu
          </v-icon>
        </v-app-bar>
        <v-main>
          <router-view></router-view>
        </v-main>
    </v-app>
</template>

<script>
  export default {
      name: 'App',
  };
</script>

<style lang="scss">
    @import "sass/variables";

    .stepper--card {
        height: 300px !important;

        @media screen and(max-width: 800px) {
            height: 500px !important;
        }
    }
</style>
