<template>
  <v-app>
    <v-app-bar app>
    </v-app-bar>
    <v-main>
      <v-container>
      <v-row no-gutters>
        <h3>zu welchem thema brauchen sie hilfe?</h3>
      </v-row>
      <v-row>
        <v-col>
          <div v-ripple class="sexschen-button">
            <v-avatar class="ma-2" size="96">
              <img
                  src="https://quickline.ch/media/r0uc4oce/icon_nav_internet.png"
              alt="internet">
            </v-avatar>
            <span>Internet</span>
          </div>
        </v-col>
        <v-col>
          <div v-ripple class="sexschen-button">
            <v-avatar class="ma-2" size="96">
              <img
                  src="https://quickline.ch/media/r0uc4oce/icon_nav_internet.png"
                  alt="internet">
            </v-avatar>
            <span>Internet</span>
          </div>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <div v-ripple class="sexschen-button">
            <v-avatar class="ma-2" size="96">
              <img
                  src="https://quickline.ch/media/r0uc4oce/icon_nav_internet.png"
                  alt="internet">
            </v-avatar>
            <span>Internet</span>
          </div>
        </v-col>
        <v-col>
          <div v-ripple class="sexschen-button">
            <v-avatar class="ma-2" size="96">
              <img
                  src="https://quickline.ch/media/r0uc4oce/icon_nav_internet.png"
                  alt="internet">
            </v-avatar>
            <span>Internet</span>
          </div>
        </v-col>
      </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style lang="scss">
.sexschen-button{
  display: flex;
  flex-direction: column;
  align-items: center;
  color: #d40037;
  font-size: 1.25rem;
}
</style>
