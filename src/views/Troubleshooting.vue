<template>
  <v-container>
    <v-col>
      <h3>Wir haben einen Lösungsvorschlag für Sie!</h3>

      <p>Basierend auf Ihren Angaben "{{ userQuery }}" haben wir folgenden Vorschlag für Sie gefunden:</p>

      <v-expansion-panels
        v-model="panels"
      >
        <v-expansion-panel
          v-for="(tlb, i) in steps"
          :key="i"
        >
          <v-expansion-panel-header v-text="tlb.title"></v-expansion-panel-header>
          <v-expansion-panel-content>
            <div class="mb-4" v-html="tlb.content"></div>

            <span class="caption mb-1">Hat das ihr Problem gelöst?</span>
            <v-row no-gutters class="justify-end">
              <v-btn text @click="nextTLB">Nein</v-btn>
              <v-btn dark color="green" @click="setSuccess">Ja!</v-btn>
            </v-row>
          </v-expansion-panel-content>
        </v-expansion-panel>

        <v-expansion-panel disabled v-if="loading">
          <v-expansion-panel-header>
            <v-progress-circular indeterminate></v-progress-circular>
          </v-expansion-panel-header>
        </v-expansion-panel>
      </v-expansion-panels>

      <v-card class="mt-5" color="green" dark v-if="flow && flow.state === Flow.STATE_SUCCESSFUL">
        <v-card-title>Geschafft!</v-card-title>
        <v-card-text>Ruf mich an, Dadday</v-card-text>
      </v-card>

      <v-card class="mt-5" color="accent" dark v-if="flow && flow.state === Flow.STATE_UNSUCCESSFUL">
        <v-card-title>Ich weiss nicht mehr weiter.</v-card-title>
        <v-card-text>Ruf mich an, Dadday</v-card-text>
      </v-card>
    </v-col>
  </v-container>
</template>

<script>
import {mapState} from 'vuex';
import { Flow } from '../services/api'

export default {
  name: 'Troubleshooting',
  data () {
    return {
      panels: 0,
      loading: false,
      Flow,
    }
  },
  computed: {
    ...mapState(['flow']),
    userQuery() {
      if (this.flow) {
        return this.flow.user_query || ''
      } else {
        return ''
      }
    },
    steps() {
      if (this.flow) {
        return this.flow.steps
      } else {
        return []
      }
    }
  },
  methods: {
    async nextTLB() {
      this.loading = true
      await this.$store.dispatch('nextTLB')
      this.loading = false
      this.panels = this.steps.length - 1
      if (this.flow && this.flow.state === Flow.STATE_UNSUCCESSFUL) this.panels = -1
    },
    async setSuccess() {
      await this.$store.dispatch('setSuccess')
      this.panels = -1
    }
  }
}
</script>

<style scoped>

</style>
