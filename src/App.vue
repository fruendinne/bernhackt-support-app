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
      <v-container class="fill-height align-start">
        <v-row no-gutters class="flex-grow-0">
          <h3>Zu welchem Thema brauchen Sie Hilfe?</h3>
        </v-row>
        <v-col>
          <div>
            <v-row>
              <v-col>
                <div class="sexschen-button">
                  <v-avatar class="ma-2" size="96">
                    <img
                        src="https://quickline.ch/media/r0uc4oce/icon_nav_internet.png"
                        alt="internet">
                  </v-avatar>
                  <span>Internet</span>
                </div>
              </v-col>
              <v-col>
                <div class="sexschen-button">
                  <v-avatar class="ma-2" size="96">
                    <img
                        src="https://quickline.ch/media/liyhf3en/icon_nav_tv.png"
                        alt="TV">
                  </v-avatar>
                  <span>TV</span>
                </div>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <div class="sexschen-button">
                  <v-avatar class="ma-2" size="96">
                    <img
                        src="https://quickline.ch/media/iv4eq3t3/icon_nav_mobile.png"
                        alt="mobile">
                  </v-avatar>
                  <span>Mobile</span>
                </div>
              </v-col>
              <v-col>
                <div class="sexschen-button">
                  <v-avatar class="ma-2" size="96">
                    <img
                        src="https://quickline.ch/media/og4jau2b/icon_nav_festnetz.png"
                        alt="festnetz">
                  </v-avatar>
                  <span>Festnetz</span>
                </div>
              </v-col>
            </v-row>
          </div>
        </v-col>
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
.sexschen-button {
  display: flex;
  flex-direction: column;
  align-items: center;
  color: #d40037;
  font-size: 1.25rem;
}
</style>
