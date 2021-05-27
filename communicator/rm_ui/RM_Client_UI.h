#ifndef RM_CLIENT_UI
#define RM_CLIENT_UI

#define Robot_ID UI_Data_RobotID_RStandard3
#define Cilent_ID UI_Data_CilentID_RStandard3 //????????????

#include "stdarg.h"
// #include "stm32f4xx.h"
// #include "usart.h"
#include <stdint.h>

#define __packed

typedef uint8_t u8;
typedef uint16_t u16;
typedef uint32_t u32;

#pragma pack(push, 1) //??1??????

#define NULL 0
#define __FALSE 100

/****************************??????*********************/
#define UI_SOF 0xA5
/****************************CMD_ID????********************/
#define UI_CMD_Robo_Exchange 0x0301
#define UI_CMD_Minimap 0x0303
#define UI_CMD_Minimap305 0x0305
/****************************????ID????********************/
#define UI_Data_ID_Del 0x100
#define UI_Data_ID_Draw1 0x101
#define UI_Data_ID_Draw2 0x102
#define UI_Data_ID_Draw5 0x103
#define UI_Data_ID_Draw7 0x104
#define UI_Data_ID_DrawChar 0x110
/****************************????????ID********************/
#define UI_Data_RobotID_RHero 1
#define UI_Data_RobotID_REngineer 2
#define UI_Data_RobotID_RStandard1 3
#define UI_Data_RobotID_RStandard2 4
#define UI_Data_RobotID_RStandard3 5
#define UI_Data_RobotID_RAerial 6
#define UI_Data_RobotID_RSentry 7
#define UI_Data_RobotID_RRadar 9
/****************************??????????ID********************/
#define UI_Data_RobotID_BHero 101
#define UI_Data_RobotID_BEngineer 102
#define UI_Data_RobotID_BStandard1 103
#define UI_Data_RobotID_BStandard2 104
#define UI_Data_RobotID_BStandard3 105
#define UI_Data_RobotID_BAerial 106
#define UI_Data_RobotID_BSentry 107
#define UI_Data_RobotID_BRadar 109
/**************************????????ID************************/
#define UI_Data_CilentID_RHero 0x0101
#define UI_Data_CilentID_REngineer 0x0102
#define UI_Data_CilentID_RStandard1 0x0103
#define UI_Data_CilentID_RStandard2 0x0104
#define UI_Data_CilentID_RStandard3 0x0105
#define UI_Data_CilentID_RAerial 0x0106
/***************************??????????ID***********************/
#define UI_Data_CilentID_BHero 0x0165
#define UI_Data_CilentID_BEngineer 0x0166
#define UI_Data_CilentID_BStandard1 0x0167
#define UI_Data_CilentID_BStandard2 0x0168
#define UI_Data_CilentID_BStandard3 0x0169
#define UI_Data_CilentID_BAerial 0x016A
/***************************???????***************************/
#define UI_Data_Del_NoOperate 0
#define UI_Data_Del_Layer 1
#define UI_Data_Del_ALL 2
/***************************??????��???__??��???********************/
#define UI_Graph_ADD 1
#define UI_Graph_Change 2
#define UI_Graph_Del 3
/***************************??????��???__???????********************/
#define UI_Graph_Line 0      //???
#define UI_Graph_Rectangle 1 //????
#define UI_Graph_Circle 2    //???
#define UI_Graph_Ellipse 3   //???
#define UI_Graph_Arc 4       //???
#define UI_Graph_Float 5     //??????
#define UI_Graph_Int 6       //????
#define UI_Graph_Char 7      //?????
/***************************??????��???__??????********************/
#define UI_Color_Main 0 //???????
#define UI_Color_Yellow 1
#define UI_Color_Green 2
#define UI_Color_Orange 3
#define UI_Color_Purplish_red 4 //????
#define UI_Color_Pink 5
#define UI_Color_Cyan 6 //???
#define UI_Color_Black 7
#define UI_Color_White 8

typedef unsigned char Uint8_t;
typedef unsigned char U8;

typedef struct
{
  u8 SOF;          //??????,???0xA5
  u16 Data_Length; //????????
  u8 Seq;          //?????
  u8 CRC8;         // CRC8��???
  u16 CMD_ID;      //????ID
} UI_Packhead;     //??

typedef struct
{
  u16 Data_ID;     //????ID
  u16 Sender_ID;   //??????ID
  u16 Receiver_ID; //??????ID
} UI_Data_Operate; //?????????

typedef struct
{
  u8 Delete_Operate; //???????
  u8 Layer;          //??????
} UI_Data_Delete;    //???????

typedef struct
{
  uint8_t graphic_name[3];
  uint32_t operate_tpye : 3;
  uint32_t graphic_tpye : 3;
  uint32_t layer : 4;
  uint32_t color : 4;
  uint32_t start_angle : 9;
  uint32_t end_angle : 9;
  uint32_t width : 10;
  uint32_t start_x : 11;
  uint32_t start_y : 11;
  int32_t graph_Float; //????????
} Float_Data;

typedef struct
{
  uint8_t graphic_name[3];
  uint32_t operate_tpye : 3;
  uint32_t graphic_tpye : 3;
  uint32_t layer : 4;
  uint32_t color : 4;
  uint32_t start_angle : 9;
  uint32_t end_angle : 9;
  uint32_t width : 10;
  uint32_t start_x : 11;
  uint32_t start_y : 11;
  uint32_t radius : 10;
  uint32_t end_x : 11;
  uint32_t end_y : 11; //???????
} Graph_Data;

typedef struct
{
  Graph_Data Graph_Control;
  uint8_t show_Data[30];
} String_Data; //????????????

struct MinimapData
{
  float x;
  float y;
  float z;
  uint8_t key;
  uint16_t id;
};

struct MinimapData305
{
  uint16_t id;
  float x;
  float y;
  float dir;
};

typedef struct
{
  uint8_t sof;          /*!< Fixed value 0xA5 */
  uint16_t data_length; /*!< Length of next data pack */
  uint8_t seq;          /*!< Pack sequene id */
  uint8_t crc8;         /*!< CRC checksum for frame header pack */
} ext_frame_header_t;

typedef struct
{
  uint16_t target_robot_ID;
  float target_position_x;
  float target_position_y;
} ext_client_map_command_t;

typedef __packed struct
{
  uint8_t graphic_name[3];
  uint32_t operate_tpye : 3;
  uint32_t graphic_tpye : 3;
  uint32_t layer : 4;
  uint32_t color : 4;
  uint32_t start_angle : 9;
  uint32_t end_angle : 9;
  uint32_t width : 10;
  uint32_t start_x : 11;
  uint32_t start_y : 11;
  uint32_t radius : 10;
  uint32_t end_x : 11;
  uint32_t end_y : 11;
} ext_client_graphic_draw_t;

typedef struct
{
  ext_frame_header_t header;
  uint16_t cmd_id;

  ext_client_map_command_t data;

  uint16_t crc16;
} ext_client_map_data_t;

#define REFEREE_FRAME_HEADER_SOF                ((uint8_t)(0xA5))

typedef enum {
    game_state                  = 0x0001,     /*!< frequency = 1Hz */
    game_result                 = 0x0002,     /*!< send at game ending */
    game_robot_survivors        = 0x0003,     /*!< frequency = 1Hz */
    event_data                  = 0x0101,     /*!< send at event changing */
    supply_projectile_action    = 0x0102,     /*!< send at action */
    supply_projectile_booking   = 0x0103,     /*!< send by user, max frequency = 10Hz */
    game_robot_state            = 0x0201,     /*!< frequency = 10Hz */
    power_heat_data             = 0x0202,     /*!< frequency = 50Hz */
    game_robot_pos              = 0x0203,     /*!< frequency = 10Hz */
    buff_musk                   = 0x0204,     /*!< send at changing */
    aerial_robot_energy         = 0x0205,     /*!< frequency = 10Hz, only for aerial robot */
    robot_hurt                  = 0x0206,     /*!< send at hurting */
    shoot_data                  = 0x0207,     /*!< send at shooting */
    robot_interactive_data      = 0x0301,     /*!< send by user, max frequency = 10Hz */
} ext_cmd_id_t;

typedef enum {
    robotid_red_hero = 1,
    robotid_red_engineer = 2,
    robotid_red_infantry_1 = 3,
    robotid_red_infantry_2 = 4,
    robotid_red_infantry_3 = 5,
    robotid_red_aerial = 6,
    robotid_red_sentry = 7,
    robotid_blue_hero = 11,
    robotid_blue_engineer = 12,
    robotid_blue_infantry_1 = 13,
    robotid_blue_infantry_2 = 14,
    robotid_blue_infantry_3 = 15,
    robotid_blue_aerial = 16,
    robotid_blue_sentry = 17,

    clientid_red_hero = 0x0101,
    clientid_red_engineer = 0x0102,
    clientid_red_infantry_1 = 0x0103,
    clientid_red_infantry_2 = 0x0104,
    clientid_red_infantry_3 = 0x0105,
    clientid_red_aerial = 0x0106,
    clientid_blue_hero = 0x0111,
    clientid_blue_engineer = 0x0112,
    clientid_blue_infantry_1 = 0x0113,
    clientid_blue_infantry_2 = 0x0114,
    clientid_blue_infantry_3 = 0x0115,
    clientid_blue_aerial = 0x0116,
} ext_id_t;

typedef __packed struct
{
  ext_client_graphic_draw_t graphic_data_struct;
  uint8_t data[30];
} ext_client_custom_character_t;

typedef __packed struct
{
  ext_frame_header_t header;
  uint16_t cmd_id;

  uint16_t data_id; /*!< range 0x200~0x2FF */
  uint16_t sender_id;
  uint16_t robot_id;
  ext_client_custom_character_t character_data; /*!< max data length = 43byte */

  uint16_t crc16;
} ext_robot_character_data_t;

typedef __packed struct
{
ext_client_graphic_draw_t graphic_data_struct[7];
}ext_client_custom_graphic_seven_t;

typedef __packed struct {
		ext_frame_header_t  					header;
		uint16_t											cmd_id;
	
    uint16_t            					data_id;            /*!< range 0x200~0x2FF */
    uint16_t            					sender_id;
    uint16_t            					robot_id;
    ext_client_custom_graphic_seven_t			graphic_data;          /*!< max data length = 13byte */
	
		uint16_t                      crc16;
} ext_robot_sev_graphic_data_t;

void UI_Delete(char *buffer, u8 Del_Operate, u8 Del_Layer);
void Line_Draw(Graph_Data *image, char imagename[3], u32 Graph_Operate,
               u32 Graph_Layer, u32 Graph_Color, u32 Graph_Width, u32 Start_x,
               u32 Start_y, u32 End_x, u32 End_y);
int UI_ReFresh(char *buffer, int cnt, ...);
unsigned char Get_CRC8_Check_Sum_UI(unsigned char *pchMessage,
                                    unsigned int dwLength,
                                    unsigned char ucCRC8);
uint16_t Get_CRC16_Check_Sum_UI(uint8_t *pchMessage, uint32_t dwLength,
                                uint16_t wCRC);
void Circle_Draw(Graph_Data *image, char imagename[3], u32 Graph_Operate,
                 u32 Graph_Layer, u32 Graph_Color, u32 Graph_Width, u32 Start_x,
                 u32 Start_y, u32 Graph_Radius);
void Rectangle_Draw(Graph_Data *image, char imagename[3], u32 Graph_Operate,
                    u32 Graph_Layer, u32 Graph_Color, u32 Graph_Width,
                    u32 Start_x, u32 Start_y, u32 End_x, u32 End_y);
void Float_Draw(Float_Data *image, char imagename[3], u32 Graph_Operate,
                u32 Graph_Layer, u32 Graph_Color, u32 Graph_Size,
                u32 Graph_Digit, u32 Graph_Width, u32 Start_x, u32 Start_y,
                float Graph_Float);
void Char_Draw(String_Data *image, char imagename[3], u32 Graph_Operate,
               u32 Graph_Layer, u32 Graph_Color, u32 Graph_Size,
               u32 Graph_Digit, u32 Graph_Width, u32 Start_x, u32 Start_y,
               char *Char_Data);
int Char_ReFresh(char *buffer, String_Data string_Data);
void Arc_Draw(Graph_Data *image, char imagename[3], u32 Graph_Operate,
              u32 Graph_Layer, u32 Graph_Color, u32 Graph_StartAngle,
              u32 Graph_EndAngle, u32 Graph_Width, u32 Start_x, u32 Start_y,
              u32 x_Length, u32 y_Length);
int UI_SendMinimap(char *buffer, uint16_t id, float x, float y);
int UI_SendMinimap305(char *buffer, uint16_t id, float x, float y);

int UI_DrawCircle(char *buffer, u32 Graph_Operate,
                  u32 Graph_Layer, u32 Graph_Color, u32 Graph_Width, u32 Start_x,
                  u32 Start_y, u32 End_x, u32 End_y);

void referee_send_map(char *buf, uint16_t id, float x, float y);

void UI_DrawFloat(char *, char imagename[3], u32 Graph_Operate,
                  u32 Graph_Layer, u32 Graph_Color, u32 Graph_Size,
                  u32 Graph_Digit, u32 Graph_Width, u32 Start_x, u32 Start_y,
                  float Graph_Float);

void send_str(char *buf);
void send_multi_graphic(char * buf);
#pragma pack(pop)
#endif /* RM_CLIENT_UI */
