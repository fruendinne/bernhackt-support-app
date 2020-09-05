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
                                                <OnboardingProblemGeneral/>
                                            </v-card>
                                            <v-col class="d-flex justify-end">
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
                                                <v-btn medium text color="primary" @click="e6 = 1">Zurück</v-btn>
                                                <v-btn medium color="accent" @click="e6 = 3">Weiter</v-btn>
                                            </v-col>
                                        </v-stepper-content>

                                        <v-stepper-step :complete="e6 > 3" step="3">Überprüfung ist am Laufen
                                        </v-stepper-step>

                                        <v-stepper-content step="3">
                                            <v-card class="mb-12 stepper--card" height="300px">
                                                <OnboardingLoading/>
                                            </v-card>
                                            <v-col class="d-flex justify-end">
                                                <v-btn medium text color="primary" @click="e6 = 2">Zurück</v-btn>
                                                <v-btn medium color="accent" @click="e6 = 4">Weiter</v-btn>
                                            </v-col>
                                        </v-stepper-content>

                                        <v-stepper-step step="4">Überprüfung ist fertig</v-stepper-step>
                                        <v-stepper-content step="4">
                                            <v-card class="mb-12 stepper--card" height="300px">
                                                TODO
                                            </v-card>
                                            <v-col class="d-flex justify-end">
                                                <v-btn medium text color="primary" @click="e6 = 3">Zurück</v-btn>
                                                <v-btn medium color="accent" @click="e6 = 4">Weiter</v-btn>
                                            </v-col>
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
    import OnboardingProblemGeneral from './views/OnboardingProblemGeneral';
    import OnboardingLoading from './views/OnboardingLoading';

    export default {
        name: 'App',
        components: { OnboardingCustomerNumber, OnboardingProblemGeneral, OnboardingLoading },
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
        height: 350px !important;

        @media screen and(max-width: 800px) {
            height: 500px !important;
        }
    }
</style>
