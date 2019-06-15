import React, {Component} from 'react';
import {Platform, StyleSheet, Text, View, ScrollView} from 'react-native';
import {AppRegistry, Image, Picker, TextInput} from 'react-native';
import {Modal, TouchableHighlight, Alert, TouchableOpacity, TouchableWithoutFeedback, Rectangle, Dimensions} from 'react-native';


const SCREEN_WIDTH = Dimensions.get('window').width;
const SCREEN_HEIGHT = Dimensions.get('window').height;
const Alto = 60;
const Ancho = 200;

export default class Formulario extends Component {
    state = {
        modalVisible: false,
        pickerCarie: "default_value",
        pickerComentario: "",
    };
    setModalVisible(visible) {
        this.setState({modalVisible: visible});
    };
    setAllToDB(){
    };

    render() {
        //this.setState({pickerCarie: itemValue})}
        return (
            <View style={{marginTop: 22}}>
                <Modal
                animationType="slide"
                transparent={true}
                visible={this.state.modalVisible}
                onRequestClose={() => {
                this.setModalVisible(!this.state.modalVisible);
                }}>
                    <View style={{flex: 1,margin: 30, backgroundColor: '#f0f8ff'}}>
                        <View style={{flex: 1}}>
                            <ScrollView style={{margin:10}}>
                                <View style={{justifyContent:'center', alignItems: 'center'}}>
                                    <Text style={{color: 'midnightblue', fontWeight: 'bold', fontSize: 20}} >
                                        EDITAR PIEZA x
                                    </Text>
                                </View>

                                <View style={{flexDirection: 'row'}}>
                                    <View style={{height: Alto, justifyContent:'center', alignItems: 'center'}}>
                                        <Text>
                                            Caries:
                                        </Text>
                                    </View>

                                    <Picker
                                    selectedValue= {this.state.pickerCarie}
                                    style={{height: Alto, width: Ancho}}
                                    onValueChange={(itemValue, itemIndex) =>
                                    this.setState({pickerCarie: itemValue})}>
                                        <Picker.Item label='Sin' value= 'sin Caries'/>
                                        <Picker.Item label='Arriba' value= 'arriba'/>
                                        <Picker.Item label='Abajo' value= 'adelante'/>
                                        <Picker.Item label='Atras' value= 'atras'/>
                                        <Picker.Item label='Izquierda' value= 'izquierda'/>
                                        <Picker.Item label='Derecha' value= 'derecha'/>
                                    </Picker>
                                </View>

                                <View style={{flexDirection: 'row'}}>
                                    <View style={{height: Alto, justifyContent:'center', alignItems: 'center'}}>
                                        <Text>
                                            Caries:
                                        </Text>
                                    </View>

                                    <Picker
                                    selectedValue= {this.state.pickerCarie}
                                    style={{height: Alto, width: Ancho}}
                                    onValueChange={(itemValue, itemIndex) =>
                                    this.setState({pickerCarie: itemValue})}>
                                        <Picker.Item label='Sin' value= 'sin Caries'/>
                                        <Picker.Item label='Arriba' value= 'arriba'/>
                                        <Picker.Item label='Abajo' value= 'adelante'/>
                                        <Picker.Item label='Atras' value= 'atras'/>
                                        <Picker.Item label='Izquierda' value= 'izquierda'/>
                                        <Picker.Item label='Derecha' value= 'derecha'/>
                                    </Picker>
                                </View>

                                <TextInput
                                style={{borderColor: 'gray', borderWidth: 1}}
                                multiline = {true}
                                numberOfLines = {3}
                                placeholder = 'Escribir un Comentario'
                                onChangeText={(texto) => {
                                this.setState({pickerComentario: texto});
                                }}
                                value={this.state.pickerComentario}/>


                            </ScrollView>
                        </View>


                        <View style={{height: 50,marginBottom: 10, backgroundColor:'#f0f8ff', flexDirection: 'row' }}>
                            <TouchableOpacity
                            onPress={() => {
                                this.setModalVisible(!this.state.modalVisible);
                            }}
                            style={{justifyContent:'center', alignItems: 'center', margin: 5, flex:1,backgroundColor:'midnightblue'}}>
                                <Text style={{color: '#f0f8ff', fontWeight: 'bold', fontSize: 24, justifyContent:'center', alignItems: 'center'}}>
                                    Confirmar
                                </Text>
                            </TouchableOpacity>
                            <TouchableOpacity
                            onPress={() => {
                                this.setModalVisible(!this.state.modalVisible);
                            }}
                            style={{justifyContent:'center', alignItems: 'center', margin: 5, flex:1, backgroundColor:'orange'}}>
                                <Text style={{color: '#f0f8ff', fontWeight: 'bold', fontSize: 24, justifyContent:'center', alignItems: 'center'}}>
                                    Cancelar
                                </Text>
                            </TouchableOpacity>
                        </View>

                    </View>
                </Modal>


                <View style={{height: 50, margin: 30,marginBottom:10,marginTop:5, backgroundColor: 'orange'}}>
                    <TouchableHighlight
                    onPress={() => {
                        this.setModalVisible(true);
                    }}
                    style={{justifyContent:'center', alignItems: 'center'}}>
                        <Text style={{color: '#f0f8ff', fontWeight: 'bold', fontSize: 20, justifyContent:'center', alignItems: 'center'}}>
                            EDITAR FICHA
                        </Text>
                    </TouchableHighlight>
                </View>
            </View>
        );
    }
};