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
                                {this.diente} {"\n"}
								{estaPieza} {"\n"}
								Tiene caries: {this.state.caries} {"\n"}
								Tiene tapaduras: {this.state.tapadura} {"\n"}
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
		  <View style={{flex: 1, backgroundColor: '#2196F388'}}/>
        </TouchableHighlight>

      </View>
    );
  }
};