import React, {Component} from 'react';
import {Platform, StyleSheet, Text, View, ScrollView} from 'react-native';
import {AppRegistry, Image, Dimensions } from 'react-native';



export default class FichaPaciente extends Component {

    const SCREEN_WIDTH = Dimensions.get('window').width;
    const SCREEN_HEIGHT = Dimensions.get('window').height;

    render() {
        return (

            <View>
                <Text>
                    Ficha Tratamiendo
                </Text>

                <ScrollView>

                    <View>
                        <Text>
                            Esta ficha solo muestra la informacion del tratamiento en proceso
                        </Text>
                        <View>
                            <View>

                            </View>
                        </View>
                    </View>
                </ScrollView>
                <TouchableOpacity
                onPress={() => {}}
                style={{justifyContent:'center', alignItems: 'center'}}>
                    <Text style={{color: '#f0f8ff', fontWeight: 'bold', fontSize: 30}}>
                        Entendido
                    </Text>
                </TouchableOpacity>
            </View>

        );
    }
}
