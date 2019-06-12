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
		  base_url: "http://127.0.0.1:8000/"
	
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
							onPress={() => {
								Alert.alert('Pieza 11, incisivo');
							}}
							title=" "
							color="#00000000"
							tipoPiezaDental='incisivo'
							
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', top: 0.07816*SCREEN_HEIGHT, left: 0.30947*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 12, incisivo');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', top: 0.11666*SCREEN_HEIGHT, left: 0.23157*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 13, canino');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '10%', position: 'absolute', top: 0.16333*SCREEN_HEIGHT, left: 0.18947*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 14, premolar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', top: 0.21000*SCREEN_HEIGHT, left: 0.16842*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 15, premolar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '13%', position: 'absolute', top: 0.26833*SCREEN_HEIGHT, left: 0.12631*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 16, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '13%', position: 'absolute', top: 0.33833*SCREEN_HEIGHT, left: 0.11578*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 17, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '10%', position: 'absolute', top: 0.4025*SCREEN_HEIGHT, left: 0.11578*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 18, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					
					
					
					<View style={{height: '10%', width: '8%', position: 'absolute', top: 0.06416*SCREEN_HEIGHT, right: 0.42105*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 21, incisivo');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', top: 0.07816*SCREEN_HEIGHT, right: 0.32210*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 22, incisivo');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', top: 0.11083*SCREEN_HEIGHT, right: 0.24631*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 23, canino');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '10%', position: 'absolute', top: 0.154*SCREEN_HEIGHT, right: 0.2*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 24, premolar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', top: 0.19833*SCREEN_HEIGHT, right: 0.16842*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 25, premolar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '13%', position: 'absolute', top: 0.25666*SCREEN_HEIGHT, right: 0.13684*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 26, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '13%', position: 'absolute', top: 0.32666*SCREEN_HEIGHT, right: 0.11578*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 27, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '10%', position: 'absolute', top: 0.39083*SCREEN_HEIGHT, right: 0.12*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 28, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					
					
					
					<View style={{height: '10%', width: '6%', position: 'absolute', bottom: -0.00583*SCREEN_HEIGHT, left: 0.45684*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 41, incisivo');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '6%', position: 'absolute', bottom: 0, left: 0.38947*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 42, incisivo');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '7%', position: 'absolute', bottom: 0.01166*SCREEN_HEIGHT, left: 0.31578*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 43, canino');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '9%', position: 'absolute', bottom: 0.05833*SCREEN_HEIGHT, left: 0.26736*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 44, premolar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '9%', position: 'absolute', bottom: 0.10850*SCREEN_HEIGHT, left: 0.22526*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 45, premolar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '11%', position: 'absolute', bottom: 0.175*SCREEN_HEIGHT, left: 0.17894*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 46, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '12%', position: 'absolute', bottom: 0.25666*SCREEN_HEIGHT, left: 0.15157*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 47, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '10%', position: 'absolute', bottom: 0.32666*SCREEN_HEIGHT, left: 0.12631*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 48, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					
					
					
					<View style={{height: '10%', width: '6%', position: 'absolute', bottom: -0.00583*SCREEN_HEIGHT, right: 0.42105*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 31, incisivo');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '6%', position: 'absolute', bottom: 0, right: 0.35789*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 32, incisivo');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '7%', position: 'absolute', bottom: 0.021*SCREEN_HEIGHT, right: 0.28421*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 33, canino');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '8%', position: 'absolute', bottom: 0.07*SCREEN_HEIGHT, right: 0.23789*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 34, premolar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '9%', position: 'absolute', bottom: 0.12016*SCREEN_HEIGHT, right: 0.20421*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 35, premolar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '12%', position: 'absolute', bottom: 0.18433*SCREEN_HEIGHT, right: 0.16210*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 36, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '12%', position: 'absolute', bottom: 0.25666*SCREEN_HEIGHT, right: 0.13052*SCREEN_WIDTH}}>
						<Button
							onPress={() => {
								Alert.alert('Pieza 37, molar');
							}}
							title=" "
							color="#00000000"
						/>
					</View>
					<View style={{height: '10%', width: '10%', position: 'absolute', bottom: 0.33833*SCREEN_HEIGHT, right: 0.12*SCREEN_WIDTH}}>
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
