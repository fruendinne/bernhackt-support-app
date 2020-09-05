<template>
  <div>
    <h2 class="text-hyphens">Hmm...Auf den ersten Blick konnten wir nichts ungewöhnliches feststellen.</h2>
    <h3 class="text-hyphens">Können Sie uns Ihr Problem schildern?</h3>
    <v-col>
    <v-row>
      <v-text-field
          color="primary"
          placeholder="Suche">
      </v-text-field>
      <v-btn fab dark color ="accent">
        <v-icon dark>mdi-magnify</v-icon>
      </v-btn>
    </v-row>
    </v-col>
    <div class="d-flex d-inline-flex flex-wrap">
      <v-chip class="ma-1" color="primary" outlined>Router brennt</v-chip>
      <v-chip class="ma-1" color="primary" outlined>Kann nicht auf Instagram</v-chip>
      <v-chip class="ma-1" color="primary" outlined>Rote LED blinkt</v-chip>
      <v-chip class="ma-1" color="primary" outlined>Mein Internet ist zu langsam</v-chip>
      <v-chip class="ma-1" color="primary" outlined>Modem funktioniert nicht mehr</v-chip>
      <v-chip class="ma-1" color="primary" outlined>Kein Internet</v-chip>
      <v-chip class="ma-1" color="primary" outlined>IMAP-Konto kann nicht eingerichtet werden</v-chip>
      <v-chip class="ma-1" color="primary" outlined>Portfreigabe</v-chip>
      <v-chip class="ma-1" color="primary" outlined>Virus im Router</v-chip>
      <v-chip class="ma-1" color="primary" outlined>Wie installiere ich mein Modem?</v-chip>
    </div>
  </div>
</template>

<script>
export default {
  name: "Pfjorschliegle"
}
</script>

<style scoped>

</style>
