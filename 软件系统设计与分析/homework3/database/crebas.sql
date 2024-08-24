/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2023/10/15 0:35:42                           */
/*==============================================================*/


/*==============================================================*/
/* Table: Relationship_1                                        */
/*==============================================================*/
create table Relationship_1
(
   uid                  int not null,
   rid                  int
);

alter table Relationship_1
   add primary key (uid);

/*==============================================================*/
/* Table: Relationship_3                                        */
/*==============================================================*/
create table Relationship_3
(
   l_id                 int not null,
   rid                  int
);

alter table Relationship_3
   add primary key (l_id);

/*==============================================================*/
/* Table: audio_data                                            */
/*==============================================================*/
create table audio_data
(
   d_id                 int not null,
   m_id                 int,
   uid                  varchar(32),
   a_time               float,
   a_name               varchar(45),
   a_link               varchar(45)
);

alter table audio_data
   add primary key (d_id);

/*==============================================================*/
/* Table: caption_data                                          */
/*==============================================================*/
create table caption_data
(
   d_id                 int not null,
   uid                  varchar(32),
   c_name               varchar(45),
   c_link               varchar(45)
);

alter table caption_data
   add primary key (d_id);

/*==============================================================*/
/* Table: data                                                  */
/*==============================================================*/
create table data
(
   d_id                 int not null,
   uid                  int
);

alter table data
   add primary key (d_id);

/*==============================================================*/
/* Table: lisence                                               */
/*==============================================================*/
create table lisence
(
   l_id                 int not null,
   op_id                int,
   ob_id                int,
   lname                varchar(45)
);

alter table lisence
   add primary key (l_id);

/*==============================================================*/
/* Table: music                                                 */
/*==============================================================*/
create table music
(
   m_id                 int not null,
   d_id                 int,
   cap_d_id             int,
   aud_d_id             int,
   m_kind               varchar(45)
);

alter table music
   add primary key (m_id);

/*==============================================================*/
/* Table: object                                                */
/*==============================================================*/
create table object
(
   ob_id                int not null,
   ob_name              varchar(45),
   ob_link              varchar(45)
);

alter table object
   add primary key (ob_id);

/*==============================================================*/
/* Table: operation                                             */
/*==============================================================*/
create table operation
(
   op_id                int not null,
   op_name              varchar(45),
   op_link              varchar(45)
);

alter table operation
   add primary key (op_id);

/*==============================================================*/
/* Table: role                                                  */
/*==============================================================*/
create table role
(
   rid                  int not null,
   rname                varchar(10),
   rlevel               int,
   rid_father           int
);

alter table role
   add primary key (rid);

/*==============================================================*/
/* Table: singer_data                                           */
/*==============================================================*/
create table singer_data
(
   d_id                 int not null,
   uid                  varchar(32),
   s_name               varchar(45),
   s_brief              varchar(45),
   s_age                int,
   s_intime             date
);

alter table singer_data
   add primary key (d_id);

/*==============================================================*/
/* Table: user                                                  */
/*==============================================================*/
create table user
(
   uid                  int not null,
   uid2                 int,
   usex                 tinyint,
   uname                varchar(25),
   upassword            varchar(25),
   uemail               varchar(25),
   uphone               numeric(15,0)
);

alter table user
   add primary key (uid);

alter table Relationship_1 add constraint FK_Relationship_1 foreign key (uid)
      references user (uid) on delete restrict on update restrict;

alter table Relationship_1 add constraint FK_Relationship_2 foreign key (rid)
      references role (rid) on delete restrict on update restrict;

alter table Relationship_3 add constraint FK_Relationship_4 foreign key (rid)
      references role (rid) on delete restrict on update restrict;

alter table Relationship_3 add constraint FK_Relationship_5 foreign key (l_id)
      references lisence (l_id) on delete restrict on update restrict;

alter table audio_data add constraint FK_Inheritance_1 foreign key (d_id)
      references data (d_id) on delete restrict on update restrict;

alter table audio_data add constraint FK_Relationship_11 foreign key (m_id)
      references music (m_id) on delete restrict on update restrict;

alter table caption_data add constraint FK_Inheritance_2 foreign key (d_id)
      references data (d_id) on delete restrict on update restrict;

alter table data add constraint FK_Relationship_8 foreign key (uid)
      references user (uid) on delete restrict on update restrict;

alter table lisence add constraint FK_Relationship_6 foreign key (op_id)
      references operation (op_id) on delete restrict on update restrict;

alter table lisence add constraint FK_Relationship_7 foreign key (ob_id)
      references object (ob_id) on delete restrict on update restrict;

alter table music add constraint FK_Relationship_10 foreign key (aud_d_id)
      references audio_data (d_id) on delete restrict on update restrict;

alter table music add constraint FK_Relationship_12 foreign key (d_id)
      references singer_data (d_id) on delete restrict on update restrict;

alter table music add constraint FK_Relationship_9 foreign key (cap_d_id)
      references caption_data (d_id) on delete restrict on update restrict;

alter table singer_data add constraint FK_Inheritance_3 foreign key (d_id)
      references data (d_id) on delete restrict on update restrict;

