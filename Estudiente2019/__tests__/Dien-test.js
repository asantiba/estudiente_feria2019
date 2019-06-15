import React, {Component} from 'react';
import ModalDiente from "./Components/modal";
import {Dimensions, Platform, StyleSheet, Text, View, Image, ImageBackground, AppRegistry, Alert, Button, TouchableWithoutFeedback} from 'react-native';


class dien-test extends React.Component {
  render() {
    return (
      <View style={{ flex: 1, flexDirection: "row" , alignItems: 'center', justifyContent: 'center' }}>
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
        </View>


        <View style={{ flex: 1, flexDirection: "column" , alignItems: 'center', justifyContent: 'center' }}>
        </View>
            <Image source={require('./images/Logo.jpg')} style={{height: '55%', width: '100%'}}/>
      </View>
    );
  }
}