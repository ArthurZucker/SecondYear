################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../source/Audio.cpp \
../source/Livre.cpp \
../source/Numeric.cpp \
../source/Papier.cpp \
../source/Periodique.cpp \
../source/Video.cpp \
../source/adherent.cpp \
../source/bibli.cpp \
../source/document.cpp 

OBJS += \
./source/Audio.o \
./source/Livre.o \
./source/Numeric.o \
./source/Papier.o \
./source/Periodique.o \
./source/Video.o \
./source/adherent.o \
./source/bibli.o \
./source/document.o 

CPP_DEPS += \
./source/Audio.d \
./source/Livre.d \
./source/Numeric.d \
./source/Papier.d \
./source/Periodique.d \
./source/Video.d \
./source/adherent.d \
./source/bibli.d \
./source/document.d 


# Each subdirectory must supply rules for building sources it contributes
source/%.o: ../source/%.cpp
	@echo 'Building file: $<'
	@echo 'Invoking: Cross G++ Compiler'
	g++ -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


