import React, {Component} from 'react';
import {Platform, StyleSheet, Text, View, ScrollView} from 'react-native';
import {AppRegistry, Image } from 'react-native';
import {Modal, TouchableHighlight, Alert, TouchableOpacity, TouchableWithoutFeedback, Rectangle, Dimensions} from 'react-native';
//import ModelView from 'react-native-gl-model-view';
import { Animated, Easing } from 'react-native';


 // Pal modelo 3d po choro!!!!

// Para que el modelo dental se ajuste relativo a la pantalla:
const SCREEN_WIDTH = Dimensions.get('window').width;
const SCREEN_HEIGHT = Dimensions.get('window').height;

export default class ModalDiente extends Component {
	
	componentDidMount() {
		this.cargarDatosJSON();
	}
	
	/* Carga informacion proveniente del JSON
	-------------------------------------------- */
	cargarDatosJSON() {
		if (this.props.miJSON.tieneCaries) {
			this.setState({
				caries: "Si"
			});
		} else {
			this.setState({
				caries: "No"
			});
		}
		
		if (this.props.miJSON.tieneTapadura) {
			this.setState({
				tapadura: "Si"
			});
		} else {
			this.setState({
				tapadura: "No"
			});
		}
	};
	//--------------------------------------------

  diente=null;
  imgPieza=null;
  state = {
    modalVisible: false,
  };
  setModalVisible(visible) {
    this.setState({modalVisible: visible});
  };
  setdienteModel(id){

  };
  setDiente(pieza){
    this.diente = pieza;
    switch (pieza){
        case 'molar':
            this.piezadiente= require('./images/molar.png');
            //this.piezadiente= require('./obj/molar.obj');
            break;
        case 'premolar':
            this.piezadiente= require('./images/premolar.png');
            //this.piezadiente= require('./obj/premolar.obj');
            break;
        case 'canino':
            this.piezadiente=require('./images/canino.png');
            //this.piezadiente= require('./obj/canino.obj');
            break;
        case 'incisivo':
            this.piezadiente=require('./images/incisivo.png');
            //this.piezadiente= require('./obj/incisivo.obj');
            break;
    };
  };

  render() {
    let pic = {
              uri: './images/placeholder.png'
            };
	let estaPieza = 'Pieza '+this.props.idPiezaDental;
	switch (this.props.idPiezaDental){
        case '11':
            this.imgPieza= require('./images/DientesImg/iu1.png');
            break;
        case '12':
            this.imgPieza= require('./images/DientesImg/iu2.png');
            break;
        case '13':
            this.imgPieza= require('./images/DientesImg/iu3.png');
            break;
        case '14':
            this.imgPieza= require('./images/DientesImg/iu4.png');
            break;
        case '15':
            this.imgPieza= require('./images/DientesImg/iu5.png');
            break;
        case '16':
            this.imgPieza= require('./images/DientesImg/iu6.png');
            break;
        case '17':
            this.imgPieza= require('./images/DientesImg/iu7.png');
            break;
        case '18':
            this.imgPieza= require('./images/DientesImg/iu8.png');
            break;
        case '21':
            this.imgPieza= require('./images/DientesImg/u1.png');
            break;
        case '22':
            this.imgPieza= require('./images/DientesImg/u2.png');
            break;
        case '23':
            this.imgPieza= require('./images/DientesImg/u3.png');
            break;
        case '24':
            this.imgPieza= require('./images/DientesImg/u4.png');
            break;
        case '25':
            this.imgPieza= require('./images/DientesImg/u5.png');
            break;
        case '26':
            this.imgPieza= require('./images/DientesImg/u6.png');
            break;
        case '27':
            this.imgPieza= require('./images/DientesImg/u7.png');
            break;
        case '28':
            this.imgPieza= require('./images/DientesImg/u8.png');
            break;
        case '31':
            this.imgPieza= require('./images/DientesImg/iD1.png');
            break;
        case '32':
            this.imgPieza= require('./images/DientesImg/iD2.png');
            break;
        case '33':
            this.imgPieza= require('./images/DientesImg/iD3.png');
            break;
        case '34':
            this.imgPieza= require('./images/DientesImg/iD4.png');
            break;
        case '35':
            this.imgPieza= require('./images/DientesImg/iD5.png');
            break;
        case '36':
            this.imgPieza= require('./images/DientesImg/iD6.png');
            break;
        case '37':
            this.imgPieza= require('./images/DientesImg/iD7.png');
            break;
        case '38':
            this.imgPieza= require('./images/DientesImg/iD8.png');
            break;
        case '41':
            this.imgPieza= require('./images/DientesImg/D1.png');
            break;
        case '42':
            this.imgPieza= require('./images/DientesImg/D2.png');
            break;
        case '43':
            this.imgPieza= require('./images/DientesImg/D3.png');
            break;
        case '44':
            this.imgPieza= require('./images/DientesImg/D4.png');
            break;
        case '45':
            this.imgPieza= require('./images/DientesImg/D5.png');
            break;
        case '46':
            this.imgPieza= require('./images/DientesImg/D6.png');
            break;
        case '47':
            this.imgPieza= require('./images/DientesImg/D7.png');
            break;
        case '48':
            this.imgPieza= require('./images/DientesImg/D8.png');
            break;
      };
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
                                {this.diente}
                            </Text>
                            <Text>
                                {estaPieza}
                            </Text>
                        </View>
                        <View>
                            <Text>
                                Tiene caries: {this.state.caries}
                            </Text>
                            <Text>
                                Tiene tapaduras: {this.state.tapadura}
                            </Text>
                        </View>
                    </View>
                </View>


                <View style={{flex: 1, marginTop: 10, margin:10,}}>
                    <View style={{flex: 1, backgroundColor: '#f0f8ff', marginTop: 5}}>
                        <View style={{margin: 10 , marginBottom:3}}>
                            <ScrollView >
                                <Text style={{fontWeight: 'bold', color:'midnightblue',  fontSize: 20}}>
									Informacion: {this.props.miJSON.descripcion}
								</Text>
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
          style={{width: 0.08*SCREEN_WIDTH, height: 0.05*SCREEN_HEIGHT}}>
		  <View style={{flex: 1, backgroundColor: '#2196F300'}}>
		         <Image source={this.imgPieza} style={{width: 0.08*SCREEN_WIDTH, height: 0.05*SCREEN_HEIGHT}}/>
		  </View>
        </TouchableHighlight>

      </View>
    );
  }
};