import React, {Component} from 'react';
import {Platform, StyleSheet, Text, View, ScrollView} from 'react-native';
import {AppRegistry, Image, Picker, TextInput} from 'react-native';
import {Modal, TouchableHighlight, Alert, TouchableOpacity, TouchableWithoutFeedback, Rectangle, Dimensions} from 'react-native';


const SCREEN_WIDTH = Dimensions.get('window').width;
const SCREEN_HEIGHT = Dimensions.get('window').height;
const Alto = 60;
const Ancho = 200;

export default class FormDiente extends Component {
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
        this.setState({pickerCarie: this.props.estadoDiente});
        this.setState({pickerComentario: this.props.comentarioDiente});

        return (
            <View style={{justifyContent:'center', alignItems: 'center'}}>
                <Modal
                animationType="slide"
                transparent={true}
                visible={this.state.modalVisible}
                onRequestClose={() => {
                this.setModalVisible(!this.state.modalVisible);
                }}>
                    <View style={{margin: 30, backgroundColor: '#f0f8ff'}}>
                        <View style={{flex: 1}}>
                            <ScrollView style={{margin:10}}>
                                <View style={{justifyContent:'center', alignItems: 'center'}}>
                                    <Text style={{color: 'midnightblue', fontWeight: 'bold', fontSize: 20}} >
                                        EDITAR PIEZA {this.props.idDiente}
                                    </Text>
                                    <Text style={{color: 'midnightblue', fontWeight: 'bold', fontSize: 10}} >
                                        {this.props.tipoDiente}
                                    </Text>
                                </View>


                                /* Esto esta modularizado para copiar desde aqui */
                                <View style={{flexDirection: 'row'}}>
                                    <View style={{height: Alto, justifyContent:'center', alignItems: 'center'}}>
                                        <Text>
                                            Estado del diente:
                                        </Text>
                                    </View>
                                    <Picker
                                    selectedValue= {this.state.pickerCarie}
                                    style={{height: Alto, width: Ancho}}
                                    onValueChange={(itemValue, itemIndex) =>
                                    this.setState({pickerCarie: itemValue})}>
                                        <Picker.Item label='Sano' value= 'sin_Caries'/>
                                        <Picker.Item label='Carie Arriba' value= 'carie_arriba'/>
                                        <Picker.Item label='Carie Adelante' value= 'carie_adelante'/>
                                        <Picker.Item label='Carie Atras' value= 'carie_atras'/>
                                        <Picker.Item label='Carie Izquierda' value= 'carie_izquierda'/>
                                        <Picker.Item label='Carie Derecha' value= 'carie_derecha'/>
                                    </Picker>
                                </View>
                                /* Hasta aqui */


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
                                this.props.estadoDiente= this.state.pickerCarie;
                                this.props.comentarioDienteDiente= this.state.pickerComentario;
                            }}
                            style={{justifyContent:'center', alignItems: 'center', margin: 5, flex:1,backgroundColor:'midnightblue'}}>
                                <Text style={{color: '#f0f8ff', fontWeight: 'bold', fontSize: 20, justifyContent:'center', alignItems: 'center'}}>
                                    Confirmar cambios
                                </Text>
                            </TouchableOpacity>
                            <TouchableOpacity
                            onPress={() => {
                                this.setModalVisible(!this.state.modalVisible);
                                this.setState({pickerCarie: this.props.estadoDiente});
                                this.setState({pickerComentario: this.props.comentarioDienteDiente});
                            }}
                            style={{justifyContent:'center', alignItems: 'center', margin: 5, flex:1, backgroundColor:'orange'}}>
                                <Text style={{color: '#f0f8ff', fontWeight: 'bold', fontSize: 20, justifyContent:'center', alignItems: 'center'}}>
                                    Cancelar
                                </Text>
                            </TouchableOpacity>
                        </View>

                    </View>
                </Modal>


                <View style={{height: 50, backgroundColor: 'orange', justifyContent:'center', alignItems: 'center'}}>
                    <TouchableHighlight
                    onPress={() => {
                        this.setModalVisible(true);
                    }}
                    style={{justifyContent:'center', alignItems: 'center'}}>
                        <Text style={{color: '#f0f8ff', fontWeight: 'bold', fontSize: 20, justifyContent:'center', alignItems: 'center'}}>
                            Editar
                        </Text>
                    </TouchableHighlight>
                </View>
            </View>
        );
    }
};