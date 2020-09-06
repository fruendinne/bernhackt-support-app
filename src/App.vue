<template>
    <v-app>
        <v-main>
            <v-container class="fill-height pa-0 align-start">
                <v-stepper v-model="e6" vertical class="elevation-0">
                    <v-stepper-step :complete="e6 > 1" step="1">Wo liegt das Problem?</v-stepper-step>
                    <v-stepper-content step="1">
                        <OnboardingProblemGeneral @select="e6 = 2"/>
                    </v-stepper-content>

                    <v-stepper-step :complete="e6 > 2" step="2">Verbindungsüberprüfung</v-stepper-step>
                    <v-stepper-content step="2">
                        <OnboardingCustomerNumber/>
                        <v-row no-gutters class="justify-end">
                            <v-btn text @click="e6 = 4">Überspringen</v-btn>
                            <v-btn medium color="accent" @click="e6 = 3">Weiter</v-btn>
                        </v-row>
                    </v-stepper-content>

                    <v-stepper-step :complete="e6 > 3" step="3">Überprüfung ist am Laufen</v-stepper-step>
                    <v-stepper-content step="3">
                        <OnboardingLoading v-if="e6 === 3" @ready="e6 = 4"/>
                    </v-stepper-content>

                    <v-stepper-step step="4">Überprüfung ist fertig</v-stepper-step>
                    <v-stepper-content step="4">
                      <RProjibliesmies/>
                      <v-row no-gutters class="justify-end">
                            <v-btn text @click="e6 = 3">Zurück</v-btn>
                            <v-btn color="accent" @click="e6 = 5">Weiter</v-btn>
                        </v-row>
                    </v-stepper-content>

                    <v-stepper-step step="5">Schritt 5</v-stepper-step>
                    <v-stepper-content step="5">
                      <v-card class="mb-12 stepper--card" height="300px">
                        <Pfjorschliegle/>
                      </v-card>
                    </v-stepper-content>
                  </v-stepper>
                </v-stepper>
            </v-container>
        </v-main>
    </v-app>
</template>

<script>
    import OnboardingCustomerNumber from './views/OnboardingCustomerNumber';
    import Pfjorschliegle from "@/views/Pfjorschliegle";
    import OnboardingProblemGeneral from './views/OnboardingProblemGeneral';
    import OnboardingLoading from './views/OnboardingLoading';
    import RProjibliesmies from '@/views/R-projibliesmies';

    export default {
        name: 'App',
        components: { Pfjorschliegle, OnboardingCustomerNumber, OnboardingProblemGeneral, OnboardingLoading, RProjibliesmies },
        data() {
            return {
                e6: 1,
            };
        },
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
