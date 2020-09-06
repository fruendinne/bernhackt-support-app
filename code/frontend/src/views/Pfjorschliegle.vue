<template>
  <div>
    <h2 class="text-hyphens">Hmm... Auf den ersten Blick konnten wir nichts Ungewöhnliches feststellen.</h2>
    <h3 class="text-hyphens">Können Sie uns Ihr Problem schildern?</h3>
    <v-col>
    <v-row>
      <v-text-field
          color="primary"
          placeholder="Suche"
          v-model="query"
      >
      </v-text-field>
      <v-btn fab dark color ="accent" @click="$emit('input', query)">
        <v-icon dark>mdi-magnify</v-icon>
      </v-btn>
    </v-row>
    </v-col>
    <div class="d-flex d-inline-flex flex-wrap">
      <v-chip class="ma-1" color="primary" outlined @click="$emit('input', 'Router brennt')">Router brennt</v-chip>
      <v-chip class="ma-1" color="primary" outlined @click="$emit('input', 'Kann nicht auf Instagram')">Kann nicht auf Instagram</v-chip>
      <v-chip class="ma-1" color="primary" outlined @click="$emit('input', 'Rote LED blinkt')">Rote LED blinkt</v-chip>
      <v-chip class="ma-1" color="primary" outlined @click="$emit('input', 'Mein Internet ist zu langsam')">Mein Internet ist zu langsam</v-chip>
      <v-chip class="ma-1" color="primary" outlined @click="$emit('input', 'Modem funktioniert nicht mehr')">Modem funktioniert nicht mehr</v-chip>
      <v-chip class="ma-1" color="primary" outlined @click="$emit('input', 'Kein Internet')">Kein Internet</v-chip>
      <v-chip class="ma-1" color="primary" outlined @click="$emit('input', 'Kann IMAP-Konto nicht einrichten')">Kann IMAP-Konto nicht einrichten</v-chip>
      <v-chip class="ma-1" color="primary" outlined @click="$emit('input', 'Portfreigabe')">Portfreigabe</v-chip>
      <v-chip class="ma-1" color="primary" outlined @click="$emit('input', 'Virus im Router')">Virus im Router</v-chip>
      <v-chip class="ma-1" color="primary" outlined @click="$emit('input', 'Wie installiere ich mein Modem?')">Wie installiere ich mein Modem?</v-chip>
    </div>
  </div>
</template>

<script>
export default {
  name: "Pfjorschliegle",
  data () {
    return {
      query: ''
    };
  },
}
</script>

<style scoped>

</style>
