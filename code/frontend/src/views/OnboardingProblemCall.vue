<template>
  <div>
  <h2 class="text-hyphens">Ouch! Da scheint etwas auf unserer Seite nicht geklappt zu haben.</h2>
  <p class="text-hyphens">Unser Servicemitarbeiter wird sich in den nächsten 30 Minuten telefonisch bei Ihnen melden.</p>
    <h3 class="text-hyphens">Unter welcher Nummer können wir Sie erreichen?</h3>
    <v-text-field
        color="primary"
        label="Telefonnummer">
    </v-text-field>
  </div>
</template>

<script>
export default {
name: "OnboardingProblemCall"
}
</script>

<style scoped>

</style>
