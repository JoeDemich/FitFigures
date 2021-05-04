CREATE TABLE "User Details" (
	"UID" VARCHAR(128),
	"Name" VARCHAR(64) NOT NULL,
	"DOB" DATE NOT NULL,
	"Weight" integer NOT NULL,
	"Feet" integer NOT NULL,
	"Inches" integer NOT NULL,
	CONSTRAINT "User Details_pk" PRIMARY KEY ("UID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Interests" (
	"UID" varchar(128),
	"General Fitness" BOOLEAN NOT NULL,
	"Weight Loss" BOOLEAN NOT NULL,
	"Strength Training" BOOLEAN NOT NULL,
	"Endurance" BOOLEAN NOT NULL,
	"Calisthenics" BOOLEAN NOT NULL,
	"Athletics" BOOLEAN NOT NULL,
	"Bodybuilding" BOOLEAN NOT NULL,
	"Martial Arts" BOOLEAN NOT NULL,
	CONSTRAINT "Interests_pk" PRIMARY KEY ("UID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Stats" (
	"UID" VARCHAR(128),
	"Max Bench Press" integer,
	"Max Deadlift" integer,
	"Max Squat" integer,
	"Max Overhead Press" integer,
	"Max Push-ups" integer,
	"Max Pull-ups" integer,
	"Max Dips" integer,
	"Max Squats" integer,
	"Total Weight Used" integer,
	"Total Cardio Distance" DECIMAL,
	"Total Cardio Time" TIME,
	"Number of Workouts" integer,
	"Average Workouts Per Week" DECIMAL,
	"Longest Workout Streak" integer,
	"Longest Rest Streak" integer,
	"Total Weight Lost/Gained" integer,
	CONSTRAINT "Stats_pk" PRIMARY KEY ("UID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Workouts" (
	"UID" VARCHAR(128) NOT NULL UNIQUE,
	"Date" DATE NOT NULL UNIQUE,
	CONSTRAINT "Workouts_pk" PRIMARY KEY ("UID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Workout Details" (
	"Date" DATE NOT NULL ,
	"Exercise" VARCHAR(128) NOT NULL,
	"Set/Interval" integer NOT NULL,
	"Reps" integer,
	"Weight" integer,
	"Distance" DECIMAL,
	"Time" TIME,
	CONSTRAINT "Workout Details_pk" PRIMARY KEY ("Date")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Selected Stats" (
	"UID" VARCHAR(128) UNIQUE,
	"Max Bench Press" BOOLEAN UNIQUE,
	"Max Deadlift" BOOLEAN UNIQUE,
	"Max Squat" BOOLEAN UNIQUE,
	"Max Overhead Press" BOOLEAN UNIQUE,
	"Max Push-ups" BOOLEAN NOT NULL UNIQUE,
	"Max Pull-ups" BOOLEAN NOT NULL UNIQUE,
	"Max Dips" BOOLEAN NOT NULL UNIQUE,
	"Max Squats" BOOLEAN NOT NULL UNIQUE,
	"Total Weight Used" BOOLEAN NOT NULL UNIQUE,
	"Total Cardio Distance" BOOLEAN NOT NULL UNIQUE,
	"Total Cardio Time" BOOLEAN NOT NULL UNIQUE,
	"Number of Workouts" BOOLEAN NOT NULL UNIQUE,
	"Average Workouts Per Week" BOOLEAN NOT NULL UNIQUE,
	"Longest Workout Streak" BOOLEAN NOT NULL UNIQUE,
	"Longest Rest Streak" BOOLEAN NOT NULL UNIQUE,
	"Total Weight Lost/Gained" BOOLEAN NOT NULL UNIQUE,
	CONSTRAINT "Selected Stats_pk" PRIMARY KEY ("UID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Users" (
	"UID" VARCHAR(128) NOT NULL,
	CONSTRAINT "Users_pk" PRIMARY KEY ("UID")
) WITH (
  OIDS=FALSE
);



ALTER TABLE "User Details" ADD CONSTRAINT "User Details_fk0" FOREIGN KEY ("UID") REFERENCES "Users"("UID");

ALTER TABLE "Interests" ADD CONSTRAINT "Interests_fk0" FOREIGN KEY ("UID") REFERENCES "Users"("UID");

ALTER TABLE "Stats" ADD CONSTRAINT "Stats_fk0" FOREIGN KEY ("UID") REFERENCES "Users"("UID");

ALTER TABLE "Workouts" ADD CONSTRAINT "Workouts_fk0" FOREIGN KEY ("UID") REFERENCES "Users"("UID");

ALTER TABLE "Workout Details" ADD CONSTRAINT "Workout Details_fk0" FOREIGN KEY ("Date") REFERENCES "Workouts"("Date");

ALTER TABLE "Selected Stats" ADD CONSTRAINT "Selected Stats_fk0" FOREIGN KEY ("UID") REFERENCES "Users"("UID");
