<template>
    <v-app>
        <v-main>
            <v-container>
                <v-row>
                    <v-col>
                        <h2>Verbindungsüberprüfung</h2>
                        <p>Lassen Sie ihre Verbindung auf mögliche Störungen überprüfen. Wenn Sie das nicht möchten,
                            können Sie die Verbindungsprüfung überspringen.</p>
                        <h3>Geben Sie Ihre Kundennummer ein</h3>
                        <v-text-field
                                color="primary"
                                label="Kundennummer">
                        </v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col class="d-flex justify-end">
                        <v-btn medium text="true" color="primary">Überspringen</v-btn>
                        <v-btn medium color="accent">Weiter</v-btn>
                    </v-col>
                </v-row>
            </v-container>

        </v-main>
    </v-app>
</template>

<script>
    export default {
        name: 'App',
    };
</script>

<style lang="scss">
    @import "sass/variables";
</style>
