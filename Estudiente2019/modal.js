import React, {Component} from 'react';
import {Platform, StyleSheet, Text, View, ScrollView} from 'react-native';
import {AppRegistry, Image } from 'react-native';
import {Modal, TouchableHighlight, Alert, TouchableOpacity, TouchableWithoutFeedback, Rectangle} from 'react-native';

export default class ModalDiente extends Component {

  diente='';
  piezadiente='';
  state = {
    modalVisible: false,
  };
  setModalVisible(visible) {
    this.setState({modalVisible: visible});
  };
  setDiente(pieza){
    this.diente = pieza;
    switch (pieza){
        case 'molar':
            this.piezadiente= require('./images/molar.png');
            break;
        case 'premolar':
            this.piezadiente= require('./images/premolar.png');
            break;
        case 'canino':
            this.piezadiente=require('./images/canino.png');
            break;
        case 'incisivo':
            this.piezadiente=require('./images/incisivo.png');
            break;
    };
  };

  render() {
    let pic = {
              uri: './images/placeholder.png'
            };
	let estaPieza = 'Pieza '+this.props.idPiezaDental;
    return (
      <View style={{marginTop: 22}}>
        <Modal
          animationType="slide"
          transparent={false}
          visible={this.state.modalVisible}
          onRequestClose={() => {this.setModalVisible(!this.state.modalVisible)}}>
          <View style={{flex: 1, backgroundColor: '#f0f8ff'}}>
            <View  style={{flex: 1, marginTop: 22, margin:10, marginBottom:10, backgroundColor:'lightskyblue'}}>


                <View style={{flexDirection: 'row',  margin:10}}>

                    <Image source={this.piezadiente} style={{width: 200, height: 200}}/>

                    <View style={{flex: 1, margin:5 ,marginTop:0, marginBottom:0, flexDirection: 'column', backgroundColor: '#f0f8ff'}}>
                        <View style={{justifyContent:'center', alignItems: 'center'}} >
                            <Text style={{fontWeight: 'bold', color:'midnightblue',  fontSize: 20}}>
                                {this.diente} {estaPieza}
                            </Text>
                        </View>
                    </View>
                </View>


                <View style={{flex: 1, marginTop: 10, margin:10,}}>
                    <Text style={{fontWeight: 'bold', color:'midnightblue',  fontSize: 20}}>
                        Informacion: Tiene caries en palatino
                    </Text>
                    <View style={{flex: 1, backgroundColor: '#f0f8ff', marginTop: 5}}>
                        <View style={{margin: 10 , marginBottom:3}}>
                            <ScrollView >
                                <View style={{height: 500, backgroundColor: 'orange'}} />
                                <View style={{height: 500, backgroundColor: '#f0f8ff'}} />
                            </ScrollView>
                        </View>
                    </View>
                </View>

                <View style={{height: 50, margin: 30,marginBottom:10,marginTop:5, backgroundColor: 'orange'}}>
                       <TouchableOpacity
                       onPress={() => {this.setModalVisible(!this.state.modalVisible);}}
                       style={{justifyContent:'center', alignItems: 'center'}}>
                           <Text style={{color: '#f0f8ff',
                           fontWeight: 'bold',
                           fontSize: 30}}>
                              Entendido
                           </Text>
                       </TouchableOpacity>
                </View>
            </View>
          </View>
        </Modal>


        <TouchableHighlight
          onPress={() => {
            this.setModalVisible(true);
            this.setDiente(this.props.tipoPiezaDental);
          }}
          style={{width: 35, height: 40}}>
		  <View style={{flex: 1, backgroundColor: '#2196F388'}}/>
        </TouchableHighlight>

      </View>
    );
  }
};