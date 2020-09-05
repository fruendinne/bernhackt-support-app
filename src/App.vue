<template>
  <v-app>
    <v-main>
      <div class="flex-column d-flex align-content-center">
        <h3>Wir überprüfen nun Ihre
          Verbindung zu unseren Systemen.
          Bitte haben Sie einen
          Moment Geduld.</h3>
        <v-row align-content="center" justify="center">
        <v-col cols="6">
          <v-progress-linear
                  indeterminate
                  color="red"
                  rounded
                  height="6"
          ></v-progress-linear>
        </v-col>
        </v-row>
      </div>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
};
</script>
