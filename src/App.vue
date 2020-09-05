<template>
    <v-app>
        <v-main>
            <v-container class="fill-height">
                <v-col class="align-center">
                    <v-row no-gutters>
                        <v-col>

                            <div id="app">
                                <v-app id="inspire">
                                    <v-stepper v-model="e6" vertical>
                                        <v-stepper-step :complete="e6 > 1" step="1">
                                            Wo liegt das Problem?
                                        </v-stepper-step>

                                        <v-stepper-content step="1">
                                            <v-card class="mb-12 stepper--card">
                                                <OnboardingCustomerNumber/>
                                            </v-card>
                                            <v-col class="d-flex justify-end">
                                                <v-btn medium text color="primary" @click="e6 = 2">Überspringen
                                                </v-btn>
                                                <v-btn medium color="accent" @click="e6 = 2">Weiter</v-btn>
                                            </v-col>
                                        </v-stepper-content>

                                        <v-stepper-step :complete="e6 > 2" step="2">Verbindungsüberprüfung
                                        </v-stepper-step>

                                        <v-stepper-content step="2">
                                            <v-card class="mb-12 stepper--card" height="300px">
                                                <OnboardingCustomerNumber/>
                                            </v-card>
                                            <v-col class="d-flex justify-end">
                                                <v-btn medium text color="primary" @click="e6 = 4">Überspringen</v-btn>
                                                <v-btn medium color="accent" @click="e6 = 3">Weiter</v-btn>
                                            </v-col>
                                        </v-stepper-content>

                                        <v-stepper-step :complete="e6 > 3" step="3">Überprüfung ist am Laufen
                                        </v-stepper-step>

                                        <v-stepper-content step="3">
                                            <v-card class="mb-12 stepper--card" height="300px">
                                                <OnboardingCustomerNumber/>
                                            </v-card>
                                            <v-col class="d-flex justify-end">
                                                <v-btn medium text color="primary" @click="e6 = 2">Zurück</v-btn>
                                                <v-btn medium color="accent" @click="e6 = 4">Weiter</v-btn>
                                            </v-col>
                                        </v-stepper-content>

                                        <v-stepper-step step="4">Schritt 4</v-stepper-step>
                                        <v-stepper-content step="4">
                                            <v-card class="mb-12 stepper--card" height="300px">
                                                <OnboardingCustomerNumber/>
                                            </v-card>
                                            <v-btn color="primary" @click="e6 = 5">Continue</v-btn>
                                            <v-btn text>Cancel</v-btn>
                                        </v-stepper-content>
                                      <v-stepper-step step="5">Schritt 5</v-stepper-step>
                                      <v-stepper-content step="5">
                                        <v-card class="mb-12 stepper--card" height="300px">
                                          <Pfjorschliegle/>
                                        </v-card>
                                      </v-stepper-content>
                                    </v-stepper>
                                </v-app>
                            </div>
                        </v-col>
                    </v-row>
                </v-col>
            </v-container>
        </v-main>
    </v-app>
</template>

<script>
    import OnboardingCustomerNumber from './views/OnboardingCustomerNumber';
    import Pfjorschliegle from "@/views/Pfjorschliegle";

    export default {
        name: 'App',
        components: {Pfjorschliegle, OnboardingCustomerNumber },
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
