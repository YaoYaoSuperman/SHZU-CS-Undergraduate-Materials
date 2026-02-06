/*==============================================================*/
/* DBMS name:      Microsoft SQL Server 2008                    */
/* Created on:     2023/3/26 0:32:24                            */
/*==============================================================*/


if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('class') and o.name = 'FK_CLASS_Á¥Êô_DEPT')
alter table class
   drop constraint FK_CLASS_Á¥Êô_DEPT
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('student') and o.name = 'FK_STUDENT_ÊôÓÚ_CLASS')
alter table student
   drop constraint FK_STUDENT_ÊôÓÚ_CLASS
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('teacher') and o.name = 'FK_TEACHER_Æ¸ÈÎ_DEPT')
alter table teacher
   drop constraint FK_TEACHER_Æ¸ÈÎ_DEPT
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('ÊÚ¿Î') and o.name = 'FK_ÊÚ¿Î_ÊÚ¿Î_COURSE')
alter table ÊÚ¿Î
   drop constraint FK_ÊÚ¿Î_ÊÚ¿Î_COURSE
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('ÊÚ¿Î') and o.name = 'FK_ÊÚ¿Î_ÊÚ¿Î2_TEACHER')
alter table ÊÚ¿Î
   drop constraint FK_ÊÚ¿Î_ÊÚ¿Î2_TEACHER
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('Ñ¡ĞŞ') and o.name = 'FK_Ñ¡ĞŞ_Ñ¡ĞŞ_COURSE')
alter table Ñ¡ĞŞ
   drop constraint FK_Ñ¡ĞŞ_Ñ¡ĞŞ_COURSE
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('Ñ¡ĞŞ') and o.name = 'FK_Ñ¡ĞŞ_Ñ¡ĞŞ2_STUDENT')
alter table Ñ¡ĞŞ
   drop constraint FK_Ñ¡ĞŞ_Ñ¡ĞŞ2_STUDENT
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('class')
            and   name  = 'Á¥Êô_FK'
            and   indid > 0
            and   indid < 255)
   drop index class.Á¥Êô_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('class')
            and   type = 'U')
   drop table class
go

if exists (select 1
            from  sysobjects
           where  id = object_id('course')
            and   type = 'U')
   drop table course
go

if exists (select 1
            from  sysobjects
           where  id = object_id('dept')
            and   type = 'U')
   drop table dept
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('student')
            and   name  = 'ÊôÓÚ_FK'
            and   indid > 0
            and   indid < 255)
   drop index student.ÊôÓÚ_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('student')
            and   type = 'U')
   drop table student
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('teacher')
            and   name  = 'Æ¸ÈÎ_FK'
            and   indid > 0
            and   indid < 255)
   drop index teacher.Æ¸ÈÎ_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('teacher')
            and   type = 'U')
   drop table teacher
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('ÊÚ¿Î')
            and   name  = 'ÊÚ¿Î2_FK'
            and   indid > 0
            and   indid < 255)
   drop index ÊÚ¿Î.ÊÚ¿Î2_FK
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('ÊÚ¿Î')
            and   name  = 'ÊÚ¿Î_FK'
            and   indid > 0
            and   indid < 255)
   drop index ÊÚ¿Î.ÊÚ¿Î_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('ÊÚ¿Î')
            and   type = 'U')
   drop table ÊÚ¿Î
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('Ñ¡ĞŞ')
            and   name  = 'Ñ¡ĞŞ2_FK'
            and   indid > 0
            and   indid < 255)
   drop index Ñ¡ĞŞ.Ñ¡ĞŞ2_FK
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('Ñ¡ĞŞ')
            and   name  = 'Ñ¡ĞŞ_FK'
            and   indid > 0
            and   indid < 255)
   drop index Ñ¡ĞŞ.Ñ¡ĞŞ_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('Ñ¡ĞŞ')
            and   type = 'U')
   drop table Ñ¡ĞŞ
go

/*==============================================================*/
/* Table: class                                                 */
/*==============================================================*/
create table class (
   cid                  char(10)             not null,
   did                  char(10)             null,
   cname                varchar(20)          not null,
   cmentor              varchar(20)          not null,
   did¡®                 char(10)             not null,
   constraint PK_CLASS primary key nonclustered (cid)
)
go

/*==============================================================*/
/* Index: Á¥Êô_FK                                                 */
/*==============================================================*/
create index Á¥Êô_FK on class (
did ASC
)
go

/*==============================================================*/
/* Table: course                                                */
/*==============================================================*/
create table course (
   coid                 char(10)             not null,
   coname               varchar(20)          not null,
   cocredit             decimal(3,1)         not null,
   cotype               char(10)             not null,
   copid                char(10)             not null,
   constraint PK_COURSE primary key nonclustered (coid)
)
go

/*==============================================================*/
/* Table: dept                                                  */
/*==============================================================*/
create table dept (
   did                  char(10)             not null,
   dname                varchar(20)          not null,
   dhead                varchar(20)          not null,
   constraint PK_DEPT primary key nonclustered (did)
)
go

/*==============================================================*/
/* Table: student                                               */
/*==============================================================*/
create table student (
   sid                  char(10)             not null,
   cid                  char(10)             null,
   sname                varchar(20)          not null,
   ssex                 char(2)              not null,
   sbirth               datetime             not null,
   "cid'"               char(10)             not null,
   constraint PK_STUDENT primary key nonclustered (sid)
)
go

/*==============================================================*/
/* Index: ÊôÓÚ_FK                                                 */
/*==============================================================*/
create index ÊôÓÚ_FK on student (
cid ASC
)
go

/*==============================================================*/
/* Table: teacher                                               */
/*==============================================================*/
create table teacher (
   tid                  char(10)             not null,
   did                  char(10)             null,
   tname                varchar(20)          not null,
   tsex                 char(2)              not null,
   tpro                 varchar(20)          not null,
   tdate                datetime             not null,
   "did'"               char(10)             not null,
   constraint PK_TEACHER primary key nonclustered (tid)
)
go

/*==============================================================*/
/* Index: Æ¸ÈÎ_FK                                                 */
/*==============================================================*/
create index Æ¸ÈÎ_FK on teacher (
did ASC
)
go

/*==============================================================*/
/* Table: ÊÚ¿Î                                                    */
/*==============================================================*/
create table ÊÚ¿Î (
   coid                 char(10)             not null,
   tid                  char(10)             not null,
   term                 varchar(20)          not null,
   constraint PK_ÊÚ¿Î primary key (coid, tid, term)
)
go

/*==============================================================*/
/* Index: ÊÚ¿Î_FK                                                 */
/*==============================================================*/
create index ÊÚ¿Î_FK on ÊÚ¿Î (
coid ASC
)
go

/*==============================================================*/
/* Index: ÊÚ¿Î2_FK                                                */
/*==============================================================*/
create index ÊÚ¿Î2_FK on ÊÚ¿Î (
tid ASC
)
go

/*==============================================================*/
/* Table: Ñ¡ĞŞ                                                    */
/*==============================================================*/
create table Ñ¡ĞŞ (
   coid                 char(10)             not null,
   sid                  char(10)             not null,
   grade                tinyint              not null,
   constraint PK_Ñ¡ĞŞ primary key (coid, sid, grade)
)
go

/*==============================================================*/
/* Index: Ñ¡ĞŞ_FK                                                 */
/*==============================================================*/
create index Ñ¡ĞŞ_FK on Ñ¡ĞŞ (
coid ASC
)
go

/*==============================================================*/
/* Index: Ñ¡ĞŞ2_FK                                                */
/*==============================================================*/
create index Ñ¡ĞŞ2_FK on Ñ¡ĞŞ (
sid ASC
)
go

alter table class
   add constraint FK_CLASS_Á¥Êô_DEPT foreign key (did)
      references dept (did)
go

alter table student
   add constraint FK_STUDENT_ÊôÓÚ_CLASS foreign key (cid)
      references class (cid)
go

alter table teacher
   add constraint FK_TEACHER_Æ¸ÈÎ_DEPT foreign key (did)
      references dept (did)
go

alter table ÊÚ¿Î
   add constraint FK_ÊÚ¿Î_ÊÚ¿Î_COURSE foreign key (coid)
      references course (coid)
go

alter table ÊÚ¿Î
   add constraint FK_ÊÚ¿Î_ÊÚ¿Î2_TEACHER foreign key (tid)
      references teacher (tid)
go

alter table Ñ¡ĞŞ
   add constraint FK_Ñ¡ĞŞ_Ñ¡ĞŞ_COURSE foreign key (coid)
      references course (coid)
go

alter table Ñ¡ĞŞ
   add constraint FK_Ñ¡ĞŞ_Ñ¡ĞŞ2_STUDENT foreign key (sid)
      references student (sid)
go

