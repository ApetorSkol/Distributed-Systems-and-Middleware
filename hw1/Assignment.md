The goal of the assignment is to get some basic experience with gRPC technology.

Assignment comprises of several steps where you will call methods for the gRPC server using a provided prototype. 

You will need any implementation of gRPC in order to fulfill the assignment, many common programming languages are supported directly by the Google implementation (https://grpc.io/). 


Description of the assignment

Let us have the following protobuf definition of the homework RPC service:
----------------------------------------------------------------
```
syntax="proto3";
option java_multiple_files = true;

package hw1.tasks;

message Response {
    string token = 1;
    oneof data {
        string info = 2;
        string error = 3;
    }
    reserved 4 to 6;
    oneof task {
        UnknownTask unknownTask = 7;
    }
}

message UnknownTask {
}

message BeginData {
    string email = 1;
}

service Homework {
    rpc Begin(BeginData) returns (Response);
}
```
----------------------------------------------------------------

The method Begin in service Homework accepts a BeginData message and returns a Response message.
The response contains various essential parts. The "token" represents an access identification, which you will need for the tasks. The "info" part provides a textual description of the current task, so always read the info and follow the instructions there. The info is only provided, if you successfuly fulfilled the previous task, otherwise, the "error" provides a text desribing the problem. Finally, the "task" part will contain additional data for the current task.

The service is available at the host "andromeda.fi.muni.cz" on port "58110" (should be accessible from anywhere).

For the initial Begin method, use your university email (login@mail.muni.cz) so that the successful completion of the assignment will be assigned to you. After successful completion of the homework, submit your zipped source codes to IS depository https://is.muni.cz/auth/el/1433/jaro2025/PA053/ode/ode_hw1/. You will obtain the assignment points only if both the successful completion of the assingment is logged for your email and the source codes are submitted to IS.

Note: The protobuf definition should be gradually extended using the instruction in the "info" data. The existing definitions from the previous steps remain the same.