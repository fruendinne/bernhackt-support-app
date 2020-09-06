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
                    <v-expansion-panel-header v-text="tlb.title"
                            class="expansion-panel--header"/>
                    <v-expansion-panel-content>
                        <div class="mb-4 expansion-panel--content" v-html="tlb.content"></div>
                        <v-row no-gutters class="justify-end">
                            <span class="caption mb-1 align-self-center expansion-panel--caption">Hat das ihr Problem gelöst?</span>
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
                <v-card-title>Problem gelöst!</v-card-title>
                <v-card-text>Wir hoffen, dass Sie Ihre Produkte von Quickline nun geniessen können.</v-card-text>
            </v-card>

            <v-card class="mt-5" color="accent" dark v-if="flow && flow.state === Flow.STATE_UNSUCCESSFUL">
                <v-card-title>Wir wissen gerade auch nicht mehr weiter.</v-card-title>
                <v-card-text>Unser technischer Support (Telefon 0800 84 10 20) wird Sie in den nächsten Minuten (sofern
                    währen der Öffnungszeit) kontaktieren.
                    Für die Unannehmlichkeiten entschuldigen wir uns.
                </v-card-text>
            </v-card>
        </v-col>
    </v-container>
</template>

<script>
    import { mapState } from 'vuex';
    import { Flow } from '../services/api';

    export default {
        name: 'Troubleshooting',
        data() {
            return {
                panels: 0,
                loading: false,
                Flow,
            };
        },
        computed: {
            ...mapState(['flow']),
            userQuery() {
                if (this.flow) {
                    return this.flow.user_query || '';
                } else {
                    return '';
                }
            },
            steps() {
                if (this.flow) {
                    return this.flow.steps;
                } else {
                    return [];
                }
            },
        },
        methods: {
            async nextTLB() {
                this.loading = true;
                await this.$store.dispatch('nextTLB');
                this.loading = false;
                this.panels = [this.steps.length - 1];
                if (this.flow && this.flow.state === Flow.STATE_UNSUCCESSFUL) {
                    this.panels = -1;
                }
            },
            async setSuccess() {
                await this.$store.dispatch('setSuccess');
                this.panels = -1;
            },
        },
    };
</script>

<style scoped>
    .expansion-panel--header {
        font-size: 24px;
        font-weight: bold;
    }

    .expansion-panel--content {
        font-size: 24px;
    }

    .expansion-panel--caption {
        margin-right: 8px;
    }
</style>
