<template>
  <v-container class="fill-height pa-0 align-start">
    <v-stepper v-model="step" vertical class="elevation-0">
      <v-stepper-step :complete="step > 1" step="1">Wo liegt das Problem?</v-stepper-step>
      <v-stepper-content step="1">
        <OnboardingProblemGeneral @select="selectGeneralProblem"/>
      </v-stepper-content>

      <v-stepper-step :complete="step > 2" step="2">Verbindungsüberprüfung</v-stepper-step>
      <v-stepper-content step="2">
        <OnboardingCustomerNumber/>
        <v-row no-gutters class="justify-end">
          <v-btn text @click="step = 4">Überspringen</v-btn>
          <v-btn medium color="accent" @click="step = 3">Weiter</v-btn>
        </v-row>
      </v-stepper-content>

      <v-stepper-step :complete="step > 3" step="3">Überprüfung ist am Laufen</v-stepper-step>
      <v-stepper-content step="3">
        <OnboardingLoading v-if="step === 3" @ready="testFinished"/>
      </v-stepper-content>

      <v-stepper-step step="4">Überprüfung ist fertig</v-stepper-step>
      <v-stepper-content step="4">
        <RProjibliesmies/>
        <v-row no-gutters class="justify-end">
          <v-btn text @click="step = 3">Zurück</v-btn>
          <v-btn color="accent" @click="step = 5">Weiter</v-btn>
        </v-row>
      </v-stepper-content>

      <v-stepper-step step="5">Fehlerbehebung</v-stepper-step>
      <v-stepper-content step="5">
        <Pfjorschliegle/>
      </v-stepper-content>
    </v-stepper>
  </v-container>
</template>

<script>
  import OnboardingCustomerNumber from './OnboardingCustomerNumber';
  import OnboardingProblemGeneral from './OnboardingProblemGeneral';
  import OnboardingLoading from './OnboardingLoading';
  import Pfjorschliegle from './Pfjorschliegle';
  import RProjibliesmies from './R-projibliesmies';

  export default {
    name: 'Onboarding',
    components: {
      OnboardingCustomerNumber,
      OnboardingProblemGeneral,
      OnboardingLoading,
      Pfjorschliegle,
      RProjibliesmies,
    },
    data () {
      return {
        step: 1
      }
    },
    methods: {
      selectGeneralProblem(problem) {
        this.$store.commit('setProblem', problem)
        this.step = 2
      },
      testFinished() {
        this.step = 5
        setTimeout(() => {
          this.$vuetify.goTo('.v-stepper__step--active')
        }, 500)
      }
    }
  }
</script>

<style scoped>

</style>
