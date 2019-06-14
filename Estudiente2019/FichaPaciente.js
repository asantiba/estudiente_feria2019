import React, {Component} from 'react';
import {FlatList, Image, StyleSheet, Text, View} from 'react-native';

const User = {
  nombre: 'Luis',
  apellido_paterno: 'Hevia',
  apellido_materno: null,
  rut: '12345678-9',
  sexo: 'Masculino',
  fecha_de_nacimiento: '29/02/2001',
  diagnosticado: true,
  dientes_caries: ['1,1','1,2'],
  dientes_ausentes: ['1,8','2,8','3,8','4,8'],
  validado: true
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
						<Text style={{fontSize:18}}> Edad: 18 </Text>
					</View>
				</View>
				<View style={{flex: 10, backgroundColor: 'turquoise', flexDirection: 'row'}}>
					<View style={{flex: 1, backgroundColor: 'cyan'}}>
						<Text> Dientes con caries : </Text>
						<FlatList data={User.dientes_caries} renderItem={({item}) => <Text style={styles.item}>{item}</Text>}/>
					</View>
					<View style={{flex: 1, backgroundColor: 'darkcyan'}}>
						<Text> Dientes ausentes : </Text>
						<FlatList data={User.dientes_ausentes} renderItem={({item}) => <Text style={styles.item}>{item}</Text>}/>
					</View>
				</View>
				<View style={{flex: 2, backgroundColor: 'green'}}>
						<Text> Próximo tratamiento : </Text>
						<Text> 15 de junio de 2019</Text>
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