import React, {Component} from 'react';
import {Button, FlatList, Image, StyleSheet, Text, View} from 'react-native';
import { createStackNavigator, createAppContainer } from 'react-navigation';
import axios from 'axios';

export default class FichaPaciente extends Component {
	constructor(props){
		super(props);
		this.state = {
			loading: false,
			data: [],
			dicto: {},
			error: null,
			refreshing: false,
		}
	}
	componentDidMount() {
		const self = this;
		axios.get('http://192.168.0.12:8000/get_paciente/')
		.then((response) => {
		  this.setState({dictos:response.data});
		  this.setState({loading:true})
		 // alert(response.data["11"].estado) // response.data[id del diente].[llave a la que se quiere entrar]
		  ;
		})
		.catch(error => {
		  console.log(error);
		});
	  }
	render() {
		var User = this.state.dictos;
		return(
          	<View style={{flex: 1}}>
				<View style={{flex: 2, backgroundColor: 'darkturquoise', flexDirection: 'row'}}>
					<View style={{flex: 1}}>
						<Image source= {require('./images/pacienteficha.png')} style={{width: 80, height: 80}} />
					</View>
					{this.state.loading ?(
					<View style={{flex: 4,  alignItems: 'flex-end'}}>
						<Text style={{fontSize:24}}> {User[0]["nombre"]} </Text>
						<Text style={{fontSize:18}}> Rut: {User[0]["idpaciente"]} </Text>
						<Text style={{fontSize:18}}> Edad: {User[0]["edad"]} </Text>
					</View>):(<View></View>)}
				</View>
				<View style={{flex: 10, backgroundColor: 'turquoise', flexDirection: 'row'}}>
					<View style={{flex: 1, backgroundColor: 'cyan'}}>
						<Button
				          title="Revisar último tratamiento"
				          onPress={() => this.props.navigation.navigate('UltimoTratamiento', User[0]['idpaciente'])} //Esto pasa el parametro del rut a "tratamiento"
				        />
				        <Button
				          title="Revisar tratamientos anteriores"
				          onPress={() => alert('No hay más tratamientos para este paciente.')}
				        />
					</View>
				</View>
			</View>
			
		);
	}
}

const styles = StyleSheet.create({
  item: {
    padding: 1,
    fontSize: 18,
    height: 44,
  },
})