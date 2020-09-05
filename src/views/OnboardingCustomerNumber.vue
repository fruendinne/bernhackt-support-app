<template>
    <v-app>
        <v-main>
            <v-container>
                <v-col>
                    <v-row no-gutters>
                        <v-col>
                            <h2 class="text-hyphens">Verbindungsüberprüfung</h2>
                            <p class="text-hyphens">Lassen Sie ihre Verbindung auf mögliche Störungen überprüfen. Wenn Sie das nicht möchten,
                                können Sie die Verbindungsprüfung überspringen.</p>
                            <h3 class="text-hyphens">Geben Sie Ihre Kundennummer ein</h3>
                            <v-text-field
                                    color="primary"
                                    label="Kundennummer">
                            </v-text-field>
                        </v-col>
                    </v-row>
                </v-col>
            </v-container>
        </v-main>
    </v-app>
</template>

<script>
    export default {
        props: {
        },
    };
</script>

<style lang="scss">
    @import "../sass/variables";

    .text-hyphens {
        hyphens: auto;
    }
</style>
