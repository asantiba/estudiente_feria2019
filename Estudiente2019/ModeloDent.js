/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React, {Component} from 'react';
import {Platform, StyleSheet, Text, View, Image, ImageBackground, AppRegistry, Alert, Button, TouchableWithoutFeedback} from 'react-native';


export default class ModeloDental extends Component {
	render() {
		return (
			<View style={{
				flex: 1,
				alignItems: 'center',
				justifyContent: 'center'
			}}>
				<ImageBackground source={require('./images/modeloDental.png')} style={{height: '100%', width: '100%', alignItems: 'center', justifyContent: 'center'}}>
					
					<View style={{height: '10%', width: '8%', position: 'absolute', top: 60, left: 190}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 11, incisivo');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', top: 67, left: 147}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 12, incisivo');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', top: 100, left: 110}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 13, canino');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '10%', position: 'absolute', top: 140, left: 90}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 14, premolar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', top: 180, left: 80}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 15, premolar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '13%', position: 'absolute', top: 230, left: 60}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 16, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '13%', position: 'absolute', top: 290, left: 55}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 17, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '10%', position: 'absolute', top: 345, left: 55}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 18, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					
					
					
					<View style={{height: '10%', width: '8%', position: 'absolute', top: 55, right: 200}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 21, incisivo');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', top: 67, right: 153}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 22, incisivo');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', top: 95, right: 117}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 23, canino');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '10%', position: 'absolute', top: 132, right: 95}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 24, premolar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', top: 170, right: 80}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 25, premolar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '13%', position: 'absolute', top: 220, right: 65}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 26, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '13%', position: 'absolute', top: 280, right: 55}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 27, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '10%', position: 'absolute', top: 335, right: 57}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 28, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					
					
					
					<View style={{height: '10%', width: '6%', position: 'absolute', bottom: -5, left: 217}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 41, incisivo');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '6%', position: 'absolute', bottom: 0, left: 185}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 42, incisivo');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '7%', position: 'absolute', bottom: 10, left: 150}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 43, canino');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '9%', position: 'absolute', bottom: 50, left: 127}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 44, premolar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '9%', position: 'absolute', bottom: 93, left: 107}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 45, premolar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '11%', position: 'absolute', bottom: 150, left: 85}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 46, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '12%', position: 'absolute', bottom: 220, left: 72}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 47, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '10%', position: 'absolute', bottom: 280, left: 60}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 48, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					
					
					
					<View style={{height: '10%', width: '6%', position: 'absolute', bottom: -5, right: 200}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 31, incisivo');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '6%', position: 'absolute', bottom: 0, right: 170}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 32, incisivo');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '7%', position: 'absolute', bottom: 18, right: 135}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 33, canino');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', bottom: 60, right: 113}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 34, premolar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '9%', position: 'absolute', bottom: 103, right: 97}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 35, premolar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '12%', position: 'absolute', bottom: 158, right: 77}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 36, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '12%', position: 'absolute', bottom: 220, right: 62}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 37, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '10%', position: 'absolute', bottom: 290, right: 57}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 38, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					
				</ImageBackground>
			
			</View>
		);
	}
}

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
