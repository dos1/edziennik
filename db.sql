BEGIN;
CREATE TABLE "edziennik_attendance" ("id" serial NOT NULL PRIMARY KEY, "value" boolean NOT NULL, "justified" boolean NULL);
CREATE TABLE "edziennik_grade" ("id" serial NOT NULL PRIMARY KEY, "weight" double precision NOT NULL, "value" numeric(1, 1) NOT NULL, "comment" text NOT NULL);
CREATE TABLE "edziennik_lesson" ("id" serial NOT NULL PRIMARY KEY, "date" timestamp with time zone NOT NULL);
CREATE TABLE "edziennik_student" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(64) NOT NULL, "surname" varchar(64) NOT NULL);
CREATE TABLE "edziennik_studentclass" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(16) NOT NULL, "creation_year" date NOT NULL);
CREATE TABLE "edziennik_subject" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(64) NOT NULL);
CREATE TABLE "edziennik_teacher" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(64) NOT NULL, "surname" varchar(64) NOT NULL);
CREATE TABLE "edziennik_studentclass_teachers" ("id" serial NOT NULL PRIMARY KEY, "studentclass_id" integer NOT NULL, "teacher_id" integer NOT NULL, UNIQUE ("studentclass_id", "teacher_id"));
ALTER TABLE "edziennik_studentclass" ADD COLUMN "tutor_id" integer NOT NULL;
ALTER TABLE "edziennik_studentclass" ALTER COLUMN "tutor_id" DROP DEFAULT;
ALTER TABLE "edziennik_student" ADD COLUMN "class_member_id" integer NOT NULL UNIQUE;
ALTER TABLE "edziennik_student" ALTER COLUMN "class_member_id" DROP DEFAULT;
ALTER TABLE "edziennik_lesson" ADD COLUMN "student_class_id" integer NOT NULL;
ALTER TABLE "edziennik_lesson" ALTER COLUMN "student_class_id" DROP DEFAULT;
ALTER TABLE "edziennik_lesson" ADD COLUMN "subject_id" integer NOT NULL;
ALTER TABLE "edziennik_lesson" ALTER COLUMN "subject_id" DROP DEFAULT;
ALTER TABLE "edziennik_lesson" ADD COLUMN "teacher_id" integer NOT NULL;
ALTER TABLE "edziennik_lesson" ALTER COLUMN "teacher_id" DROP DEFAULT;
ALTER TABLE "edziennik_grade" ADD COLUMN "lesson_id" integer NOT NULL;
ALTER TABLE "edziennik_grade" ALTER COLUMN "lesson_id" DROP DEFAULT;
ALTER TABLE "edziennik_grade" ADD COLUMN "student_id" integer NOT NULL;
ALTER TABLE "edziennik_grade" ALTER COLUMN "student_id" DROP DEFAULT;
ALTER TABLE "edziennik_attendance" ADD COLUMN "lesson_id" integer NOT NULL;
ALTER TABLE "edziennik_attendance" ALTER COLUMN "lesson_id" DROP DEFAULT;
ALTER TABLE "edziennik_attendance" ADD COLUMN "student_id" integer NOT NULL;
ALTER TABLE "edziennik_attendance" ALTER COLUMN "student_id" DROP DEFAULT;
ALTER TABLE "edziennik_studentclass_teachers" ADD CONSTRAINT "e_studentclass_id_1742584f406778fe_fk_edziennik_studentclass_id" FOREIGN KEY ("studentclass_id") REFERENCES "edziennik_studentclass" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "edziennik_studentclass_teachers" ADD CONSTRAINT "edziennik_s_teacher_id_3bc158115ae37763_fk_edziennik_teacher_id" FOREIGN KEY ("teacher_id") REFERENCES "edziennik_teacher" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "edziennik_studentclass_teachers_84bfbaa2" ON "edziennik_studentclass_teachers" ("studentclass_id");
CREATE INDEX "edziennik_studentclass_teachers_d9614d40" ON "edziennik_studentclass_teachers" ("teacher_id");
CREATE INDEX "edziennik_studentclass_1ba55b7f" ON "edziennik_studentclass" ("tutor_id");
ALTER TABLE "edziennik_studentclass" ADD CONSTRAINT "edziennik_stu_tutor_id_53931d8e2c52da46_fk_edziennik_teacher_id" FOREIGN KEY ("tutor_id") REFERENCES "edziennik_teacher" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "edziennik_student" ADD CONSTRAINT "e_class_member_id_372bfb39c74b6198_fk_edziennik_studentclass_id" FOREIGN KEY ("class_member_id") REFERENCES "edziennik_studentclass" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "edziennik_lesson_4ace59a9" ON "edziennik_lesson" ("student_class_id");
ALTER TABLE "edziennik_lesson" ADD CONSTRAINT "e_student_class_id_bba9df6b0243b4c_fk_edziennik_studentclass_id" FOREIGN KEY ("student_class_id") REFERENCES "edziennik_studentclass" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "edziennik_lesson_ffaba1d1" ON "edziennik_lesson" ("subject_id");
ALTER TABLE "edziennik_lesson" ADD CONSTRAINT "edziennik_l_subject_id_738712fb4140633d_fk_edziennik_subject_id" FOREIGN KEY ("subject_id") REFERENCES "edziennik_subject" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "edziennik_lesson_d9614d40" ON "edziennik_lesson" ("teacher_id");
ALTER TABLE "edziennik_lesson" ADD CONSTRAINT "edziennik_l_teacher_id_2255b90107753314_fk_edziennik_teacher_id" FOREIGN KEY ("teacher_id") REFERENCES "edziennik_teacher" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "edziennik_grade_55174b7b" ON "edziennik_grade" ("lesson_id");
ALTER TABLE "edziennik_grade" ADD CONSTRAINT "edziennik_gra_lesson_id_6ef86c800afe6cd8_fk_edziennik_lesson_id" FOREIGN KEY ("lesson_id") REFERENCES "edziennik_lesson" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "edziennik_grade_30a811f6" ON "edziennik_grade" ("student_id");
ALTER TABLE "edziennik_grade" ADD CONSTRAINT "edziennik_g_student_id_12777b1b1d4816b8_fk_edziennik_student_id" FOREIGN KEY ("student_id") REFERENCES "edziennik_student" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "edziennik_attendance_55174b7b" ON "edziennik_attendance" ("lesson_id");
ALTER TABLE "edziennik_attendance" ADD CONSTRAINT "edziennik_att_lesson_id_264d41bb9f3c100d_fk_edziennik_lesson_id" FOREIGN KEY ("lesson_id") REFERENCES "edziennik_lesson" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "edziennik_attendance_30a811f6" ON "edziennik_attendance" ("student_id");
ALTER TABLE "edziennik_attendance" ADD CONSTRAINT "edziennik_at_student_id_7b12e6a2d5c1983_fk_edziennik_student_id" FOREIGN KEY ("student_id") REFERENCES "edziennik_student" ("id") DEFERRABLE INITIALLY DEFERRED;

COMMIT;