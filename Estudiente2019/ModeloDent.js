/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React, {Component} from 'react';
import {Dimensions, Platform, StyleSheet, Text, View, Image, ImageBackground, AppRegistry, Alert, Button, TouchableWithoutFeedback} from 'react-native';
import ModalDiente from './modal';

// Para que el modelo dental se ajuste relativo a la pantalla:
const SCREEN_WIDTH = Dimensions.get('window').width;
const SCREEN_HEIGHT = Dimensions.get('window').height;

export default class ModeloDental extends Component {
	constructor(props){
		super(props);
		this.state  = {
		  loading: false,
		  data: [],
		  error: null,
		  refreshing: false,
		  base_url: "http://127.0.0.1:8000/",
		  
		  /* Se usara para hacer pruebas. Al final este JSON 
		  se debe obtener de la BD */
		  // -----------------------------------------------
		  testJson: {
			  "dientes": {
				"11" : {
					"tieneCaries": true,
					"tieneTapadura": false,
					"descripcion": "Carie mesial"
				},
				"12" : {
					"tieneCaries": true,
					"tieneTapadura": false,
					"descripcion": "Carie en palatino"
				},
				"13" : {
					"tieneCaries": false,
					"tieneTapadura": true,
					"descripcion": "Tapadura de oro"
				},
				"14" : {
					"tieneCaries": false,
					"tieneTapadura": false,
					"descripcion": "Pieza dental sana"
				},
				"15" : {
					"tieneCaries": false,
					"tieneTapadura": false,
					"descripcion": "Pieza dental sana"
				},
				"16" : {
					"tieneCaries": false,
					"tieneTapadura": false,
					"descripcion": "Pieza dental sana"
				},
				"17" : {
					"tieneCaries": false,
					"tieneTapadura": false,
					"descripcion": "Pieza dental sana"
				},
				"18" : {
					"tieneCaries": false,
					"tieneTapadura": false,
					"descripcion": "Pieza dental sana"
				}
			  }
		  }
		  // -------------------------------------------------
	
	  }}
	  componentDidMount() {
		this.fetchDataFromApi();
	  }
	  fetchDataFromApi = ()  => {
		const url = "http://127.0.0.1:8000/get_dent_list";
	
		this.setState({ loading: true });
	
		fetch(url)
		  .then(res => res.json())
		  .then(res => {
	
			this.setState({
			  data: res,
			  error: null,
			  loading: false,
			  refreshing: false
			});
		  })
		  .catch(error => {
			this.setState({ error, loading : false });
		  })
	  };
	
	  handleRefresh = () => {
		this.setState(
		  {
			refreshing: true
		  },
		  () => {
			this.fetchDataFromApi();
		  }
		);
	  };
	  
	render() {
		return (
			<View style={{
				flex: 1,
				alignItems: 'center',
				justifyContent: 'center'
			}}>
				<ImageBackground source={require('./images/modeloDent.png')} style={{height: '100%', width: '100%', alignItems: 'center', justifyContent: 'center'}}>
					
					<View style={{height: '10%', width: '8%', position: 'absolute', top: 0.01*SCREEN_HEIGHT, left: 0.42*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='incisivo'
							idPiezaDental='11'
							miJSON={this.state.testJson.dientes[11]}
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', top: 0.028*SCREEN_HEIGHT, left: 0.34*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='incisivo'
							idPiezaDental='12'
							miJSON={this.state.testJson.dientes[12]}
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', top: 0.053*SCREEN_HEIGHT, left: 0.26*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='canino'
							idPiezaDental='13'
							miJSON={this.state.testJson.dientes[13]}
						/>
					</View>
					<View style={{height: '10%', width: '10%', position: 'absolute', top: 0.088*SCREEN_HEIGHT, left: 0.214*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='premolar'
							idPiezaDental='14'
							miJSON={this.state.testJson.dientes[14]}
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', top: 0.138*SCREEN_HEIGHT, left: 0.17*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='premolar'
							idPiezaDental='15'
							miJSON={this.state.testJson.dientes[15]}
						/>
					</View>
					<View style={{height: '10%', width: '13%', position: 'absolute', top: 0.19*SCREEN_HEIGHT, left: 0.13*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='molar'
							idPiezaDental='16'
							miJSON={this.state.testJson.dientes[16]}
						/>
					</View>
					<View style={{height: '10%', width: '13%', position: 'absolute', top: 0.265*SCREEN_HEIGHT, left: 0.11*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='molar'
							idPiezaDental='17'
							miJSON={this.state.testJson.dientes[17]}
						/>
					</View>
					<View style={{height: '10%', width: '10%', position: 'absolute', top: 0.335*SCREEN_HEIGHT, left: 0.095*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='molar'
							idPiezaDental='18'
							miJSON={this.state.testJson.dientes[18]}
						/>
					</View>
					
				</ImageBackground>
			
			</View>
		);
	}
}

/*


					<View style={{height: '10%', width: '8%', position: 'absolute', top: 0.01*SCREEN_HEIGHT, right: 0.41*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='incisivo'
							idPiezaDental='21'
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', top: 0.028*SCREEN_HEIGHT, right: 0.33*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='incisivo'
							idPiezaDental='22'
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', top: 0.053*SCREEN_HEIGHT, right: 0.25*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='canino'
							idPiezaDental='23'
						/>
					</View>
					<View style={{height: '10%', width: '10%', position: 'absolute', top: 0.088*SCREEN_HEIGHT, right: 0.204*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='premolar'
							idPiezaDental='24'
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', top: 0.138*SCREEN_HEIGHT, right: 0.16*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='premolar'
							idPiezaDental='25'
						/>
					</View>
					<View style={{height: '10%', width: '13%', position: 'absolute', top: 0.19*SCREEN_HEIGHT, right: 0.08*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='molar'
							idPiezaDental='26'
						/>
					</View>
					<View style={{height: '10%', width: '13%', position: 'absolute', top: 0.265*SCREEN_HEIGHT, right: 0.055*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='molar'
							idPiezaDental='27'
						/>
					</View>
					<View style={{height: '10%', width: '10%', position: 'absolute', top: 0.335*SCREEN_HEIGHT, right: 0.065*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='molar'
							idPiezaDental='28'
						/>
					</View>
					
					
					
					
					
					<View style={{height: '10%', width: '8%', position: 'absolute', bottom: 0.025*SCREEN_HEIGHT, left: 0.42*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='incisivo'
							idPiezaDental='41'
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', bottom: 0.038*SCREEN_HEIGHT, left: 0.34*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='incisivo'
							idPiezaDental='42'
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', bottom: 0.063*SCREEN_HEIGHT, left: 0.3*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='canino'
							idPiezaDental='43'
						/>
					</View>
					<View style={{height: '10%', width: '10%', position: 'absolute', bottom: 0.098*SCREEN_HEIGHT, left: 0.235*SCREEN_WIDTH}}>
						<ModalDiente
							title=" "
							color="#00000000"
							tipoPiezaDental='premolar'
							idPiezaDental='44'
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', bottom: 0.148*SCREEN_HEIGHT, left: 0.19*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='premolar'
							idPiezaDental='45'
						/>
					</View>
					<View style={{height: '10%', width: '13%', position: 'absolute', bottom: 0.2*SCREEN_HEIGHT, left: 0.14*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='molar'
							idPiezaDental='46'
						/>
					</View>
					<View style={{height: '10%', width: '13%', position: 'absolute', bottom: 0.275*SCREEN_HEIGHT, left: 0.11*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='molar'
							idPiezaDental='47'
						/>
					</View>
					<View style={{height: '10%', width: '10%', position: 'absolute', bottom: 0.345*SCREEN_HEIGHT, left: 0.095*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='molar'
							idPiezaDental='48'
						/>
					</View>
					
					
					
					
					
					<View style={{height: '10%', width: '8%', position: 'absolute', bottom: 0.025*SCREEN_HEIGHT, right: 0.42*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='incisivo'
							idPiezaDental='31'
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', bottom: 0.038*SCREEN_HEIGHT, right: 0.34*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='incisivo'
							idPiezaDental='32'
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', bottom: 0.063*SCREEN_HEIGHT, right: 0.3*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='canino'
							idPiezaDental='33'
						/>
					</View>
					<View style={{height: '10%', width: '10%', position: 'absolute', bottom: 0.098*SCREEN_HEIGHT, right: 0.237*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='premolar'
							idPiezaDental='34'
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', bottom: 0.148*SCREEN_HEIGHT, right: 0.19*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='premolar'
							idPiezaDental='35'
						/>
					</View>
					<View style={{height: '10%', width: '13%', position: 'absolute', bottom: 0.2*SCREEN_HEIGHT, right: 0.09*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='molar'
							idPiezaDental='36'
						/>
					</View>
					<View style={{height: '10%', width: '13%', position: 'absolute', bottom: 0.275*SCREEN_HEIGHT, right: 0.05*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='molar'
							idPiezaDental='37'
						/>
					</View>
					<View style={{height: '10%', width: '10%', position: 'absolute', bottom: 0.345*SCREEN_HEIGHT, right: 0.08*SCREEN_WIDTH}}>
						<ModalDiente
							tipoPiezaDental='molar'
							idPiezaDental='38'
						/>
					</View>

*/

AppRegistry.registerComponent('TestProject', () => ModeloDental);


const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  instructions: {
    textAlign: 'center',
    color: '#333333',
    marginBottom: 5,
  },
});