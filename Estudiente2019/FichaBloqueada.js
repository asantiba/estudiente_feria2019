import React, {Component} from 'react';
import {FlatList, Image, StyleSheet, Text, View, Button} from 'react-native';

const User = {
  nombre: 'Acceso',
  rut: 'XX.XXX.XXX-X',
  apellido_paterno: 'Denegado',
  apellido_materno: null,
  edad: 'N/A'
};

export default class FichaPaciente extends Component {
	render() {
		return(
          	<View style={{flex: 1}}>
				<View style={{flex: 2, backgroundColor: 'darkturquoise', flexDirection: 'row'}}>
					<View style={{flex: 1}}>
						<Image source= {require('./images/pacienteficha.png')} style={{width: 80, height: 80}} />
					</View>
					<View style={{flex: 4,  alignItems: 'flex-end'}}>
						<Text style={{fontSize:24}}> {User.nombre} {User.apellido_paterno} {User.apellido_materno} </Text>
						<Text style={{fontSize:18}}> Rut: {User.rut} </Text>
						<Text style={{fontSize:18}}> Edad: {User.edad} </Text>
					</View>
				</View>
				<View style={{flex: 10, backgroundColor: 'turquoise', flexDirection: 'row', alignItems: 'center', justifyContent:'center'}}>
					<Button
						color='grey'
						style={{width:'20%', height:'20%'}}
						title= "Solicitar Acceso para ver la Ficha"
					/>
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